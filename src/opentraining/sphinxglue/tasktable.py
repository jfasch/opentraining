from . import utils
from . import soup
from ..project import Project
from ..person import Person
from ..task import Task
from ..group import Group
from ..errors import OpenTrainingError

from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import set_source_info
from docutils import nodes
from docutils.parsers.rst import directives 


from sphinx.util import logging
_logger = logging.getLogger(__name__)


def setup(app):
    app.add_directive('ot-tasktable', _TaskTableDirective)
    app.connect('doctree-resolved', _ev_doctree_resolved__expand_tasktable_nodes)

def _ev_doctree_resolved__expand_tasktable_nodes(app, doctree, docname):
    for n in doctree.traverse(_TaskTableNode):
        try:
            project = app.ot_soup.element_by_path(n.path, userdata=n)
        except OpenTrainingError as e:
            _logger.warning(e, location=e.userdata)
            n.replace_self([])
            continue

        table = nodes.table()
        tgroup = nodes.tgroup(cols=8)
        table += tgroup
        tgroup += nodes.colspec(colwidth=8)
        tgroup += nodes.colspec(colwidth=4)
        tgroup += nodes.colspec(colwidth=4)
        tgroup += nodes.colspec(colwidth=4)
        tgroup += nodes.colspec(colwidth=4)
        tgroup += nodes.colspec(colwidth=4)
        tgroup += nodes.colspec(colwidth=4)
        tgroup += nodes.colspec(colwidth=4)

        if 'thead':
            thead = nodes.thead()
            tgroup += thead
            row = nodes.row()
            thead += row

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('Task')

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('Implementation Points')

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('%')

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('Documentation Points')

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('%')

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('Integration Points')

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('%')

            entry = nodes.entry()
            row += entry
            entry += nodes.Text('Total %')

        if 'tbody':
            tbody = nodes.tbody()
            tgroup += tbody

            for task in project.tasks:
                row = nodes.row()
                tbody += row

                # link to task
                entry = nodes.entry()
                row += entry
                p = nodes.paragraph()
                entry += p
                p += [utils.make_reference(text=task.title,
                                           from_docname=docname, to_docname=task.docname,
                                           app=app)]

                implementation_percent, documentation_percent, integration_percent, total_percent = task.stats()

                # implementation
                entry = nodes.entry()
                row += entry
                entry += nodes.Text(str(task.implementation_points))

                entry = nodes.entry()
                row += entry
                entry += nodes.Text(str(implementation_percent))

                # documentation
                entry = nodes.entry()
                row += entry
                entry += nodes.Text(str(task.documentation_points))

                entry = nodes.entry()
                row += entry
                entry += nodes.Text(str(documentation_percent))

                # integration
                entry = nodes.entry()
                row += entry
                entry += nodes.Text(str(task.integration_points))

                entry = nodes.entry()
                row += entry
                entry += nodes.Text(str(integration_percent))

                # total
                entry = nodes.entry()
                row += entry
                entry += nodes.Text(str(total_percent))

        n.replace_self([table])

class _TaskTableNode(nodes.Element):
    def __init__(self, path):
        super().__init__(self)
        self.path = path
        
class _TaskTableDirective(SphinxDirective):
    required_arguments = 1   # path
    option_spec = {
        'sort-by': utils.list_of_elementpath,
    }

    def run(self):
        path = utils.element_path(self.arguments[0].strip())

        tasks = _TaskTableNode(path = path)
        tasks.document = self.state.document
        set_source_info(self, tasks)

        return [tasks]
