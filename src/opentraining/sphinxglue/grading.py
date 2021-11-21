from . import utils
from . import soup
from ..grading import Grading
from ..errors import OpenTrainingError

from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import set_source_info
from docutils import nodes
from docutils.parsers.rst import directives 


from sphinx.util import logging
_logger = logging.getLogger(__name__)


def setup(app):
    app.add_directive('ot-pointscollected', _PointsCollectedDirective)
    app.connect('doctree-resolved', _ev_doctree_resolved__expand_pointscollected_nodes)

def _ev_doctree_resolved__expand_pointscollected_nodes(app, doctree, docname):
    for n in doctree.traverse(_PointsCollectedNode):
        persons = []
        tasks = []
        for person in n.persons:
            try:
                persons.append(app.ot_soup.element_by_path(person, userdata=n))
            except OpenTrainingError as e:
                _logger.warning(e, location=n)
        for task in n.tasks:
            try:
                tasks.append(app.ot_soup.element_by_path(task, userdata=n))
            except OpenTrainingError as e:
                _logger.warning(e, location=n)

        grading = Grading(persons = persons, tasks = tasks)

        table = nodes.table()
        tgroup = nodes.tgroup(cols=2)
        table += tgroup
        tgroup += nodes.colspec(colwidth=8)
        tgroup += nodes.colspec(colwidth=4)

        thead = nodes.thead()
        tgroup += thead
        row = nodes.row()
        thead += row

        entry = nodes.entry()
        row += entry
        entry += nodes.Text('Person')
        entry = nodes.entry()
        row += entry
        entry += nodes.Text('Points')

        tbody = nodes.tbody()
        tgroup += tbody

        for person, points in grading.points_per_person():
            row = nodes.row()
            tbody += row

            # link to person
            entry = nodes.entry()
            row += entry
            p = nodes.paragraph()
            entry += p
            p += [utils.make_reference(
                text=f'{person.firstname} {person.lastname}',
                from_docname=docname, to_docname=person.docname,
                app=app)]

            # points
            entry = nodes.entry()
            row += entry
            entry += nodes.Text(str(points))

        n.replace_self([table])

class _PointsCollectedNode(nodes.Element):
    def __init__(self, persons, tasks, shape):
        super().__init__(self)
        self.title = None
        self.persons = persons
        self.tasks = tasks
        self.shape = shape


def _table_or_list(argument):
    return directives.choice(argument, ('table', 'list'))

class _PointsCollectedDirective(SphinxDirective):
    required_arguments = 0
    option_spec = {
        'persons': utils.list_of_elementpath,
        'tasks': utils.list_of_elementpath,
        'shape': _table_or_list,
    }

    def run(self):
        persons = self.options.get('persons')
        tasks = self.options.get('tasks')
        shape = self.options.get('shape', 'list')

        pointcollected = _PointsCollectedNode(
            persons = persons,
            tasks = tasks,
            shape = shape,
        )

        pointcollected.document = self.state.document
        set_source_info(self, pointcollected)

        return [pointcollected]
