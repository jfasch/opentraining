from opentraining.person import Person
from opentraining.task import Task
from opentraining.soup import Soup
from opentraining.grading import Grading
from opentraining import errors 

import pytest

from collections import namedtuple
import sys


_Project = namedtuple('_Project', ('faschingbauer', 'huber', 'queen', 'task_hi', 'task_lo', 'soup', 'grading'))

def _p():
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


    return _Project(
        faschingbauer = faschingbauer,
        huber = huber, 
        queen = queen,
        task_hi = task_hi,
        task_lo = task_lo,
        soup = Soup((queen, huber, faschingbauer, task_lo, task_hi)),
        grading = Grading(persons = (faschingbauer, huber, queen),
                          tasks = (task_hi, task_lo)),
    )

if __name__ == '__main__':
    try:
        p = _p()
    except errors.CompoundError as e:
        print(e)
    assert False, 'passt eh'
    sys.exit()


_p = pytest.fixture(_p)

def test_person_score(_p):
    assert _p.grading.person_score(_p.faschingbauer) == 70 * 100 # task_hi only

def test_score_table(_p):
    st = {person: score for person, score in _p.grading.score_table()}
    assert st[_p.faschingbauer] == 70*100
    assert st[_p.huber] == 90*100 + 50*100 + 10*100
    assert st[_p.queen] == 50*100 + 60*100
