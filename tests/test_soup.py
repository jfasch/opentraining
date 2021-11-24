from opentraining.group import Group
from opentraining.topic import Topic
from opentraining.soup import Soup
from opentraining.task import Task


def test_1_level():
    level1 = Group(title=None, path=['level1'], docname=None, userdata=None)
    topic = Topic(title=None, path=['level1', 'topic'], docname=None, dependencies=[], userdata=None)
    soup = Soup((level1, topic))

    assert soup.resolved
    assert level1.resolved
    assert topic.resolved

    assert soup.element_by_path(['level1', 'topic'], userdata=None) is topic
    assert soup.element_by_path(['level1'], userdata=None) is level1

def test_2_level():
    level1 = Group(title=None, path=['level1'], docname=None, userdata=None)
    level2 = Group(title=None, path=['level1', 'level2'], docname=None, userdata=None)
    topic = Topic(title=None, path=['level1', 'level2', 'topic'], docname=None, dependencies=[], userdata=None)
    soup = Soup((level1, level2, topic))

    assert soup.resolved
    assert level1.resolved
    assert level2.resolved
    assert topic.resolved

    assert soup.element_by_path(['level1', 'level2', 'topic'], userdata=None) is topic
    assert soup.element_by_path(['level1'], userdata=None) is level1
    assert soup.element_by_path(['level1', 'level2'], userdata=None) is level2

def test_iter():
    level1 = Group(title=None, path=['level1'], docname=None, userdata=None)
    topic = Topic(title=None, path=['level1', 'topic'], docname=None, dependencies=[], userdata=None)
    soup = Soup((level1, topic))

    elements = list(soup)
    assert len(elements) == 3  # including root group
    assert level1 in elements
    assert topic in elements

