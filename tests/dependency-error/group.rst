Errors from Unresolved Dependencies
===================================

.. ot-group:: opentraining.tests.dependency_error

Optimizing (well, to say the least) error handling. Before, we raised
hard errors when, for example, a dependency could not be
resolved. Raising hard errors lead Sphinx to rebuilding the entire
site - which is a lot and takes minutes for sites like
https://www.faschingbauer.me.

.. toctree::
   :maxdepth: 1

   hi
   lo

