from .element import Element
from .group import Group
from .node import Node
from .topic import Topic
from .exercise import Exercise
from .task import Task
from . import errors
from . import element

from networkx.algorithms.dag import descendants
from networkx import DiGraph
from networkx.exception import NetworkXError


class Soup:
    def __init__(self, elements):
        self._root_group = None
        self._worldgraph = None

        self._elements = set(elements)
        for e in self._elements:
            assert isinstance(e, Element), e
        self._resolve()

    @property
    def resolved(self):
        return self._root_group is not None

    def _resolve(self):
        if self._root_group is not None:
            return

        # build up hierarchy (thereby emptying self._elements)
        self._root_group = Group(
            title='Root', 
            path=(), 
            docname='', 
            userdata=None,
        )
        self._make_hierarchy()
        self._add_nodes_to_groups()
        assert len(self._elements) == 0, self._elements

        # once the elements have paths in their final hierarchy, we
        # can let them resolve their own stuff. for example, a task
        # initially refers to a person's *path* - final situation
        # should be that a task refers to the Person object directly.
        errs = []
        for element in self._root_group.iter_recursive():
            try:
                element.resolve(self)
            except errors.OpenTrainingError as e:
                errs.append(e)

        if len(errs):
            raise errors.CompoundError(
                'there were errors resolving paths of some elements', errors=errs, 
                # don't know which thing I could refer to when doing a
                # global resolve.
                userdata=None,
            )

        del self._elements
        self.worldgraph()    # only to detect missing dependencies
                             # early

    @property
    def root(self):
        return self._root_group

    def element_by_path(self, path, userdata):
        return self._root_group.element_by_path(path, userdata=userdata)

    def __iter__(self):
        return self._root_group.iter_recursive()

    def worldgraph(self):
        self._assert_resolved()
        return self._make_worldgraph()

    def subgraph(self, entrypoints, userdata):
        '''Given entrypoints, compute a subgraph of the world graph that
        contains the entrypoints and all their descendants.

        entrypoints is an iterable of element paths or elements (can
        be mixed)
        '''

        # paranoia
        for e in entrypoints:
            assert isinstance(e, Element)

        self._assert_resolved()
        world = self._make_worldgraph()

        topics = set()
        for topic in entrypoints:
            topics.add(topic)
            topics.update(descendants(world, topic))
        return world.subgraph(topics)

    def _make_worldgraph(self):
        if self._worldgraph is not None:
            return self._worldgraph

        collected_errors = []
        self._worldgraph = DiGraph()
        for elem in self._root_group.iter_recursive(cls=Node):
            if not isinstance(elem, Node):
                continue
            self._worldgraph.add_node(elem)
            for target_path in elem.dependencies:
                try:
                    target_topic = self.element_by_path(target_path, userdata=elem.userdata)
                    self._worldgraph.add_edge(elem, target_topic)
                except errors.PathNotFound as e:
                    collected_errors.append(
                        errors.DependencyError(
                            f'{elem.docname} ({elem}): dependency {target_path} not found', 
                            userdata=elem))

        if len(collected_errors) != 0:
            raise errors.CompoundError('cannot build world graph', errors=collected_errors, 
                                       # don't know which thing I could refer to when doing a
                                       # global resolve.
                                       userdata=None,
                                      )
        return self._worldgraph

    def _make_hierarchy(self):
        level = 1
        while True:
            all_groups = [g for g in self._elements if isinstance(g, Group)]
            if not all_groups:   # no more groups
                break
            level_groups = [g for g in all_groups if len(g._requested_path) == level]
            for g in level_groups:
                self._root_group.add_element(g, userdata=None)
                self._elements.remove(g)
            level += 1

    def _add_nodes_to_groups(self):
        nodes = [n for n in self._elements if isinstance(n, Element)]
        for n in nodes:
            self._root_group.add_element(n, userdata=None)
            self._elements.remove(n)
            
    def _assert_resolved(self):
        if not self.resolved:
            raise errors.NotCommitted('soup not resolved')

    def _assert_unresolved(self):
        if self.resolved:
            raise errors.AlreadyCommitted('soup already resolved')
