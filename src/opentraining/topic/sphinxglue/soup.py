from ..soup import Soup
from ..topic import Topic
from ..exercise import Exercise
from ..task import Task
from ..group import Group
from ..errors import TopicError


def sphinx_add_topic(app, docname, title, path, dependencies):
    if hasattr(app, 'ot_soup'):
        raise TopicError('Soup already created, cannot add one more topic')
    if not hasattr(app.env, 'ot_elements'):
        app.env.ot_elements = {}

    app.env.ot_elements[docname] = {
        'type': 'topic',
        'title': title,
        'path': path,
        'dependencies': dependencies,
    }

def sphinx_add_exercise(app, docname, title, path, dependencies):
    if hasattr(app, 'ot_soup'):
        raise TopicError('Soup already created, cannot add one more topic')
    if not hasattr(app.env, 'ot_elements'):
        app.env.ot_elements = {}

    app.env.ot_elements[docname] = {
        'type': 'exercise',
        'title': title,
        'path': path,
        'dependencies': dependencies,
    }

def sphinx_add_task(app, docname, title, path, dependencies, 
                    responsible, initial_estimate, spent, percent_done):
    if hasattr(app, 'ot_soup'):
        raise TopicError('Soup already created, cannot add one more topic')
    if not hasattr(app.env, 'ot_elements'):
        app.env.ot_elements = {}

    app.env.ot_elements[docname] = {
        'type': 'task',
        'title': title,
        'path': path,
        'dependencies': dependencies,
        'responsible': responsible,
        'initial_estimate': initial_estimate,
        'spent': spent,
        'percent_done': percent_done,
    }

def sphinx_add_group(app, docname, title, path):
    if hasattr(app, 'ot_soup'):
        raise TopicError('Soup already created, cannot add one more group')
    if not hasattr(app.env, 'ot_elements'):
        app.env.ot_elements = {}

    app.env.ot_elements[docname] = {
        'type': 'group',
        'title': title,
        'path': path,
    }

def sphinx_purge_doc(app, env, docname):
    if hasattr(env, 'ot_elements'):
        env.ot_elements.pop(docname, None)

def sphinx_create_soup(app):
    if hasattr(app, 'ot_soup'):
        return

    app.ot_soup = Soup()
    for docname, elem in app.env.ot_elements.items():
        ty = elem['type']
        if ty == 'topic':
            app.ot_soup.add_element(
                Topic(title=elem['title'], path=elem['path'], docname=docname,
                      dependencies=elem['dependencies']))
        elif ty == 'exercise':
            app.ot_soup.add_element(
                Exercise(title=elem['title'], path=elem['path'], docname=docname,
                         dependencies=elem['dependencies']))
        elif ty == 'task':
            app.ot_soup.add_element(
                Task(title=elem['title'],
                     path=elem['path'],
                     docname=docname,
                     dependencies=elem['dependencies'],
                     responsible=elem['responsible'],
                     initial_estimate=elem['initial_estimate'],
                     spent=elem['spent'],
                     percent_done=elem['percent_done'],
                ))
        elif ty == 'group':
            app.ot_soup.add_element(
                Group(title=elem['title'], path=elem['path'], docname=docname))
        else:
            raise TopicError(f'{docname}: unknown type "{ty}"')

    app.ot_soup.commit()
