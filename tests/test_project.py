from opentraining.person import Person
from opentraining.task import Task
from opentraining.soup import Soup
from opentraining.project import Project
from opentraining import errors 

import pytest

from collections import namedtuple
import sys


_Fixture = namedtuple('_Fixture', ('faschingbauer', 'huber', 'queen', 'task_hi', 'task_lo', 'soup', 'project'))

def _f():
    faschingbauer = Person(
        title=None,
        path=['faschingbauer'],
        docname=None,
        userdata=None,
        firstname='Joerg',
        lastname='Faschingbauer',
    )
    huber = Person(
        title=None,
        path=['huber'],
        docname=None,
        userdata=None,
        firstname='Sepp',
        lastname='Huber',
    )
    queen = Person(
        title=None,
        path=['queen'],
        docname=None,
        userdata=None,
        firstname='Elizabeth',
        lastname='Queen',
    )

    task_hi = Task(
        title=None,
        path=['task_hi'],
        docname=None, 
        dependencies=[['task_lo']],
        userdata=None,
        
        implementation_points=70, 
        implementors=[(['faschingbauer'], 100)],
        documentation_points=50, 
        documenters=[(['queen'], 100)],
        integration_points=90, 
        integrators=[(['huber'], 100)],
    )
    task_lo = Task(
        title=None,
        path=['task_lo'],
        docname=None, 
        dependencies=[],
        userdata=None,
        
        implementation_points=50,
        implementors=[(['huber'], 100)],
        documentation_points=60, 
        documenters=[(['queen'], 100)],
        integration_points=10, 
        integrators=[(['huber'], 100)],
    )

    project = Project(title=None, path=['project'], docname=None, userdata=None,
                      persons = (faschingbauer, huber, queen),
                      tasks = (task_hi, task_lo), 
                      )

    return _Fixture(
        faschingbauer = faschingbauer,
        huber = huber, 
        queen = queen,
        task_hi = task_hi,
        task_lo = task_lo,
        soup = Soup((queen, huber, faschingbauer, task_lo, task_hi, project)),
        project = project,
    )

if __name__ == '__main__':
    try:
        p = _p()
    except errors.CompoundError as e:
        print(e)
    assert False, 'passt eh'
    sys.exit()


_f = pytest.fixture(_f)

def test_resolve():
    task = Task(
        title=None,
        path=['task'],
        docname=None, 
        dependencies=[],
        userdata=None,
        
        implementation_points=50,
        implementors=[(['faschingbauer'], 100)],
        documentation_points=60, 
        documenters=[(['faschingbauer'], 100)],
        integration_points=10, 
        integrators=[(['faschingbauer'], 100)],
    )
    person = Person(
        title=None,
        path=['faschingbauer'],
        docname=None,
        userdata=None,
        firstname='Joerg',
        lastname='Faschingbauer',
    )
    project = Project(title=None, path=['project'], docname=None, userdata=None,
                      persons = [['faschingbauer']], 
                      tasks = [['task']],
                      )
    soup = Soup((task, person, project))

    # task's workers have mutated from paths to their respective
    # objects
    assert task.resolved
    assert task.implementors == [(person, 100)]
    assert task.documenters == [(person, 100)]
    assert task.integrators == [(person, 100)]

    # same with project's tasks and persons
    assert project.resolved
    assert project.persons == [person]
    assert project.tasks == [task]

def test_person_score(_f):
    assert _f.project.person_score(_f.faschingbauer) == 70 * 100 # task_hi only

def test_score_table(_f):
    st = {person: score for person, score in _f.project.score_table()}
    assert st[_f.faschingbauer] == 70*100
    assert st[_f.huber] == 90*100 + 50*100 + 10*100
    assert st[_f.queen] == 50*100 + 60*100

def test_tasks_of_person(_f):
    assert sorted(_f.project.tasks_of_person(_f.faschingbauer)) == sorted((_f.task_hi,))
