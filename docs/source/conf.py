# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import glob
import sys
sys.path.insert(0, os.path.abspath('.'))
from mdlink import run
from clear import deleteDir

from datetime import datetime
current_year = datetime.now().year


# -- Project information -----------------------------------------------------
project = 'Vistle'
author = 'Martin Aumüller, Marko Djuric, Dennis Grieger, Leyla Kern, Susanne Malheiros, Uwe Wössner'
author = 'the Vistle team'
copyright = f'2012 - {current_year}, {author}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
    'sphinx.ext.autosectionlabel',
    'html_image_processor',
]

# Tell sphinx what the primary language being documented is.
# primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
# highlight_language = 'cpp'


myst_enable_extensions = [
    'colon_fence',
]
myst_all_links_external=False
myst_heading_anchors = 3

# some meta data
language = "en"
myst_html_meta = {
    "description lang=en": "metadata description",
    "description lang=fr": "description des métadonnées",
    "keywords": "Sphinx, MyST",
    "property=og:locale":  "en_US"
}

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
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

autosectionlabel_prefix_document = True
deleteDir("../build")
# run("../..", ["docs/source/module"], "module", link_rst_only=True)

moduleDirectory = os.path.dirname(os.path.realpath(__file__)) + "/module"
for file_path in glob.glob(os.path.join(moduleDirectory, '*')):
    if os.path.isdir(file_path):
        category = os.path.basename(file_path)
        run("../..", ["docs/source/module/" + category], "module/" + category, True)        

# run("../..", ["lib/vistle"], "lib", exclude_dirs=["toml"])
# run("../..", ["app"], "app")
