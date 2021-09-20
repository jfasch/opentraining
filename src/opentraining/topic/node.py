from .element import Element


class Node(Element):
    def __init__(self, title, path, docname, dependencies, jjj):
        super().__init__(title=title, path=path, docname=docname, jjj=jjj)
        self.dependencies = dependencies
