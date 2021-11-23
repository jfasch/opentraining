from opentraining.task import Task
from opentraining.soup import Soup


def test_commit():
    t = Task(
        title=None,
        path=['task'],
        docname=None, 
        dependencies=[],
        userdata=None,
        
        implementation_points=50,
        implementors=[],
        documentation_points=60, 
        documenters=[],
        integration_points=10, 
        integrators=[],
    )

    soup = Soup((t,))
    assert soup.committed()
    assert t.committed()
