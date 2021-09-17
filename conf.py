# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import logging
import os
import sys
sys.path.insert(0, os.path.join(os.path.abspath('.'), 'src'))

# -- Project information -----------------------------------------------------
_me = 'Jörg Faschingbauer'
_canonical = 'https://www.faschingbauer.me'
project = 'OpenTraining'
author = _me
copyright = '2019-2021 (GPLv3), '+_me
html_title = project
html_baseurl = _canonical
release = version = ''

# -- General configuration ---------------------------------------------------
master_doc = 'index'
templates_path = []

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.graphviz',

    'opentraining.topic',
    'opentraining.dia',
]

exclude_patterns = [
    '_build',
    '**.ipynb_checkpoints',
]

html_context = {}
html_theme = 'sphinx_rtd_theme'
html_theme_path = []

html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': -1,
}
