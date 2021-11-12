from opentraining.soup import Soup
from opentraining.person import Person
from opentraining.task import Task
from opentraining.group import Group


def test_task_resolve_hints():
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

    soup = Soup()
    soup.add_element(implementor)
    soup.add_element(documenter)
    soup.add_element(integrator)
    soup.add_element(task)
    soup.add_element(group)
    soup.commit()

    assert task.implementors == [(implementor, 100)]
    assert task.documenters == [(documenter, 100)]
    assert task.integrators == [(integrator, 100)]

