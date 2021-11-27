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

Score Table
...........

.. code-block:: rst

   .. ot-scoretable:: opentraining.tests.project_management.project

.. ot-scoretable:: opentraining.tests.project_management.project

Project  Stats (Default: By Title, Ascending)
.............................................

.. code-block:: rst

   .. ot-project-taskstats:: opentraining.tests.project_management.project

.. ot-project-taskstats:: opentraining.tests.project_management.project

Project Stats (By Title (Default), Descending)
..............................................

.. code-block:: rst

   .. ot-project-taskstats:: opentraining.tests.project_management.project
      :sort-order: descending

.. ot-project-taskstats:: opentraining.tests.project_management.project
   :sort-order: descending

Project Stats (By Percent-Total, Descending)
............................................

.. code-block:: rst

   .. ot-project-taskstats:: opentraining.tests.project_management.project
         :sort-by: percent-total
	 :sort-order: descending

.. ot-project-taskstats:: opentraining.tests.project_management.project
      :sort-by: percent-total
      :sort-order: descending

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
