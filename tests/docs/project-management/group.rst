.. ot-group:: opentraining.tests.project_management

Project Management
==================

.. contents::
   :local:

Project Definition (Tasks and Persons by Group)
-----------------------------------------------

.. code-block:: rst

   .. ot-project:: opentraining.tests.project_management.project
      :persons: opentraining.tests.project_management
      :tasks: opentraining.tests.project_management

.. ot-project:: opentraining.tests.project_management.project
   :persons: opentraining.tests.project_management
   :tasks: opentraining.tests.project_management

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

Project Stats: Tasks (Default: By Title, Ascending)
...................................................

.. code-block:: rst

   .. ot-project-taskstats:: opentraining.tests.project_management.project

.. ot-project-taskstats:: opentraining.tests.project_management.project

Project Stats: Tasks (By Title (Default), Descending)
.....................................................

.. code-block:: rst

   .. ot-project-taskstats:: opentraining.tests.project_management.project
      :sort-order: descending

.. ot-project-taskstats:: opentraining.tests.project_management.project
   :sort-order: descending

Project Stats: Tasks (By Percent-Total, Descending)
...................................................

.. code-block:: rst

   .. ot-project-taskstats:: opentraining.tests.project_management.project
         :sort-by: percent-total
	 :sort-order: descending

.. ot-project-taskstats:: opentraining.tests.project_management.project
      :sort-by: percent-total
      :sort-order: descending

Project Stats: Persons (Default: By Name, Ascending)
....................................................

.. code-block:: rst

   .. ot-project-personstats:: opentraining.tests.project_management.project

.. ot-project-personstats:: opentraining.tests.project_management.project

Project Stats: Persons (Default: By Name, Descending)
.....................................................

.. code-block:: rst

   .. ot-project-personstats:: opentraining.tests.project_management.project
      :sort-by: name
      :sort-order: descending

.. ot-project-personstats:: opentraining.tests.project_management.project
   :sort-by: name
   :sort-order: descending

Project Stats: Persons (Default: By Total-Points, Descending)
.............................................................

.. code-block:: rst

   .. ot-project-personstats:: opentraining.tests.project_management.project
      :sort-by: points-total
      :sort-order: descending

.. ot-project-personstats:: opentraining.tests.project_management.project
   :sort-by: points-total
   :sort-order: descending


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
