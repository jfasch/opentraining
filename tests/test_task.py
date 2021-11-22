from opentraining.soup import Soup
from opentraining.person import Person
from opentraining.task import Task
from opentraining.group import Group

import pytest

from collections import namedtuple


Project = namedtuple('Project', ('implementor', 'documenter', 'integrator', 'task', 'group', 'soup'))


@pytest.fixture
def my_project():
    implementor = Person(
        title=None,
        path=['blah', 'implementor'],
        docname=None,
        userdata=None,
        firstname='Implementor',
        lastname='Of a Team',
    )
    documenter = Person(
        title=None,
        path=['blah', 'documenter'],
        docname=None,
        userdata=None,
        firstname='Documenter',
        lastname='Of a Team',
    )
    integrator = Person(
        title=None,
        path=['blah', 'integrator'],
        docname=None,
        userdata=None,
        firstname='Integrator',
        lastname='Of a Team',
    )
    task = Task(
        title=None,
        path=['blah', 'task'],
        docname=None, 
        dependencies=[],
        userdata=None,
        
        implementation_points=100, 
        implementors=[(['blah', 'implementor'], 100)],
        documentation_points=100, 
        documenters=[(['blah', 'documenter'], 100)],
        integration_points=100, 
        integrators=[(['blah', 'integrator'], 100)],
    )
    group = Group(
        title=None, 
        path=['blah'], 
        docname=None, 
        userdata=None)

    return Project(implementor = implementor,
                   documenter = documenter, 
                   integrator = integrator, 
                   task = task, 
                   group = group,
                   soup = Soup((implementor, documenter, integrator, task, group)))


def test_task_resolve_hints(my_project):
    assert my_project.task.implementors == [(my_project.implementor, 100)]
    assert my_project.task.documenters == [(my_project.documenter, 100)]
    assert my_project.task.integrators == [(my_project.integrator, 100)]

