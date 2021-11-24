Project Management
==================

.. ot-group:: opentraining.tests.project_management

``toctree``

.. toctree::
   :maxdepth: 1

   task-hi
   task-lo
   person-faschingbauer
   person-huber
   person-queen

Points Collected
----------------

Score Table: Explicit
.....................

.. ot-scoretable::
   :persons: opentraining.tests.project_management.person_faschingbauer,
	     opentraining.tests.project_management.person_huber,
	     opentraining.tests.project_management.person_queen
   :tasks: opentraining.tests.project_management.task_lo,
	   opentraining.tests.project_management.task_hi
	     
Score Table: Implicit (Persons and Tasks by Group)
..................................................

.. ot-scoretable::
   :persons: opentraining.tests.project_management
   :tasks: opentraining.tests.project_management

Dependencies
------------

``ot-graph``:

.. ot-graph::
   :entries: opentraining.tests.project_management
