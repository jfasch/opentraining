from .node import Node


class Task(Node):
    def __init__(self, 
                 title, path, docname, 
                 dependencies, userdata,

                 implementation_points, implementors,
                 documentation_points, documenters,
                 integration_points, integrators,

                 responsible, initial_estimate, spent, percent_done):

        # add persons as task dependencies
        person_dependencies = [person for person, share in implementors + documenters + integrators]

        super().__init__(
            title=title, 
            path=path, 
            docname=docname, 
            dependencies=dependencies + person_dependencies, 
            userdata=userdata)

        self.implementation_points = implementation_points
        self.documentation_points = documentation_points
        self.integration_points = integration_points

        self.implementors = implementors
        self.documenters = documenters
        self.integrators = integrators

        self.initial_estimate = float(initial_estimate)
        self.spent = float(spent)
        self.percent_done = float(percent_done)
        self.responsible = responsible

    def __str__(self):
        return 'Task:'+super().__str__()
