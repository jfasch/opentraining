Project Management
==================

.. ot-group:: opentraining.tests.project_management

``toctree``

.. toctree::
   :maxdepth: 1

   task-hi
   task-lo
   person-a
   person-b
   person-c

Points Collected
----------------

Score Table: Explicit Persons and Tasks
.......................................

.. ot-scoretable::
   :persons: opentraining.tests.project_management.person_a,
	     opentraining.tests.project_management.person_b,
	     opentraining.tests.project_management.person_c
   :tasks: opentraining.tests.project_management.task_lo,
	   opentraining.tests.project_management.task_hi
   :shape: table
	     
Score Table: Implicit - Persons and Tasks by Group
..................................................

.. ot-scoretable::
   :persons: opentraining.tests.project_management
   :tasks: opentraining.tests.project_management
   :shape: table
	     

Dependencies
------------

``ot-graph``:

.. ot-graph::
   :entries: opentraining.tests.project_management
