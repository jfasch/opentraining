from opentraining.core.soup import Soup
from opentraining.core.person import Person
from opentraining.core.task import Task
from opentraining.core.group import Group

import pytest

from collections import namedtuple


_Project = namedtuple('_Project', ('implementor', 'documenter', 'integrator', 'task', 'group', 'soup'))


@pytest.fixture
def _my_project():
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

    soup = Soup((implementor, documenter, integrator, task, group))

    return _Project(implementor = implementor,
                    documenter = documenter, 
                    integrator = integrator, 
                    task = task, 
                    group = group,
                    soup = soup,
                    )


def test_task_resolve_hints(_my_project):
    assert _my_project.task.implementors == [(_my_project.implementor, 100)]
    assert _my_project.task.documenters == [(_my_project.documenter, 100)]
    assert _my_project.task.integrators == [(_my_project.integrator, 100)]

def test_stats():
    task = Task(
        title=None,
        path=['blah', 'task'],
        docname=None, 
        dependencies=[],
        userdata=None,
        
        implementation_points=70, 
        implementors=[(['implementor1'], 30), (['implementor2'], 20)],
        documentation_points=30, 
        documenters=[(['documenter'], 30)],
        integration_points=90, 
        integrators=[(['integrator'], 10)],
    )

    implementation_percent, documentation_percent, integration_percent, total_percent = task.stats()
    assert implementation_percent == 30+20
    assert documentation_percent == 30
    assert integration_percent == 10

    total_points = 70+30+90
    gathered_points = 70*(30+20)/100 + 30*30/100 + 90*10/100

    assert total_percent == pytest.approx(gathered_points/total_points*100)
