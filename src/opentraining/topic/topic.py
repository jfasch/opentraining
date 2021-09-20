from .node import Node


class Topic(Node):
    def __init__(self, title, path, docname, dependencies, jjj):
        super().__init__(title=title, path=path, docname=docname, dependencies=dependencies, jjj=jjj)

    def __str__(self):
        return 'Topic:'+super().__str__()
