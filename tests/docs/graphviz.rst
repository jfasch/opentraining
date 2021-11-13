Trying the Graphviz Extension
=============================

Basic Functionality
===================

.. graphviz::

   digraph blah {
       "a" -> "b";
       "a" -> "c";
       "b" -> "d";
       "c" -> "d";
   }

Horizontal Overflow?
====================

Try to overflow horizontally, and see what happens. Do we scroll?

.. graphviz::

   digraph blah {
       "root" -> "00";
       "root" -> "01";
       "root" -> "02";
       "root" -> "03";
       "root" -> "04";
       "root" -> "05";
       "root" -> "06";
       "root" -> "07";
       "root" -> "08";
       "root" -> "09";
       "root" -> "10";
       "root" -> "11";
       "root" -> "12";
       "root" -> "13";
       "root" -> "14";
       "root" -> "15";
       "root" -> "16";
       "root" -> "17";
       "root" -> "18";
       "root" -> "19";
       "root" -> "20";
       "root" -> "21";
       "root" -> "22";
       "root" -> "23";
       "root" -> "24";
       "root" -> "25";
       "root" -> "26";
       "root" -> "27";
       "root" -> "28";
       "root" -> "29";
       "root" -> "30";
       "root" -> "31";
       "root" -> "32";
       "root" -> "33";
       "root" -> "34";
       "root" -> "35";
       "root" -> "36";
       "root" -> "37";
       "root" -> "38";
       "root" -> "39";
   }
