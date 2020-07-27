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
import os
import sys
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

project = os.path.basename(os.path.abspath(os.path.join('../', os.pardir)))
author = 'jarndt'
copyright = '2020, %s' % author


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
dirname = os.path.dirname(__file__)+"/../../"
projdir = os.path.dirname(dirname)
release = open(os.path.join(projdir, 'VERSION')).read().strip()
version = '.'.join(release.split('.')[:2])


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', # Core library for html generation from docstrings
    'sphinx.ext.autosummary', # Create neat summary tables
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode', # Add a link to the Python source code for classes, functions etc.
    'sphinx.ext.napoleon',
    # 'sphinx_autodoc_typehints', # no module named Automatically document param types (less noise in class signature)

]
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
html_show_sourcelink = False  # Remove 'view source code' from top of page (for html, not python)
autodoc_inherit_docstrings = True  # If no class summary, inherit base class summary


# extensions.append('autoapi.extension')
#
# autoapi_type = 'python'
# autoapi_dirs = ['../../cmdline']
# autoapi_ignore = ['__*__.py']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']