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

.. ot-pointscollected::
   :persons: opentraining.tests.project_management.person_a,
	     opentraining.tests.project_management.person_b,
	     opentraining.tests.project_management.person_c
   :tasks: opentraining.tests.project_management.task_lo,
	   opentraining.tests.project_management.task_hi
   :shape: table
	     

Dependencies
------------

``ot-graph``:

.. ot-graph::
   :entries: opentraining.tests.project_management
