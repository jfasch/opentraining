Project Management
==================

.. ot-group:: opentraining.tests.project_management

Project Definition (Tasks and Persons by Group)
-----------------------------------------------

.. code-block:: rst

   .. ot-project:: opentraining.tests.project_management.project
      :persons: opentraining.tests.project_management
      :tasks: opentraining.tests.project_management

.. ot-project:: opentraining.tests.project_management.project
   :persons: opentraining.tests.project_management
   :tasks: opentraining.tests.project_management

Score Table
...........

.. code-block:: rst

   .. ot-scoretable:: opentraining.tests.project_management.project

.. ot-scoretable:: opentraining.tests.project_management.project

Task Table
..........

.. code-block:: rst

   .. ot-tasktable:: opentraining.tests.project_management.project

.. ot-tasktable:: opentraining.tests.project_management.project

Project Definition (Tasks and Persons Enumerated Explicitly)
------------------------------------------------------------

.. code-block:: rst

   .. ot-project:: opentraining.tests.project_management.project1
      :persons: opentraining.tests.project_management.person_faschingbauer,
		opentraining.tests.project_management.person_huber,
   		opentraining.tests.project_management.person_queen
      :tasks: opentraining.tests.project_management.task_lo,
   	      opentraining.tests.project_management.task_hi

.. ot-project:: opentraining.tests.project_management.project1
   :persons: opentraining.tests.project_management.person_faschingbauer,
	     opentraining.tests.project_management.person_huber,
	     opentraining.tests.project_management.person_queen
   :tasks: opentraining.tests.project_management.task_lo,
	   opentraining.tests.project_management.task_hi

Score Table
...........

.. code-block:: rst

   .. ot-scoretable:: opentraining.tests.project_management.project1

.. ot-scoretable:: opentraining.tests.project_management.project1


.. toctree::
   :maxdepth: 1

   task-hi
   task-lo
   person-faschingbauer
   person-huber
   person-queen

Dependencies
------------

``ot-graph``:

.. ot-graph::
   :entries: opentraining.tests.project_management
