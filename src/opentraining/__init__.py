from .sphinxglue import topic
from .sphinxglue import exercise
from .sphinxglue import task
from .sphinxglue import taskmeta
from .sphinxglue import person
from .sphinxglue import group
from .sphinxglue import grouplist
from .sphinxglue import graph
from .sphinxglue import soup
from .sphinxglue import dia

def setup(app):
    app.connect('env-purge-doc', soup.sphinx_purge_doc)

    topic.setup(app)
    exercise.setup(app)
    task.setup(app)
    taskmeta.setup(app)
    person.setup(app)
    group.setup(app)
    grouplist.setup(app)
    graph.setup(app)
    dia.setup(app)


