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

print("Current working directory:", os.getcwd())
print("Python executable:", sys.executable)
print("sys.path:", sys.path)

source_suffix = ['.rst', '.md']  # Handling both reStructuredText and Markdown

sys.path.insert(0, os.path.abspath('../main/learn'))
sys.path.insert(0, os.path.abspath('../main'))



# -- Project information -----------------------------------------------------

project = 'Matilda'
copyright = '2024, Chunlei Liu, Pengyi Yang; Website constructed by Zebang Yang'
author = 'Chunlei Liu,Pengyi Yang'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Here, the autodoc allows Sphinx to automatically generate documentation from docstrings, napoleon allows Sphinx to parse Google-style docstrings, and myst_parser allows Sphinx to parse Markdown files.
extensions = [
    "sphinx_copybutton",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.autosummary",
]
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "strikethrough",
    "tasklist",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

rst_prolog = """
.. math::

   \\newcommand{\\ud}{\\mathop{}\\negthinspace\mathrm{d}}
   \\newcommand{\\pfrac}[2][x]{\\frac{\\partial #2}{\\partial #1}}
"""


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_sidebars = {
   '**': ['globaltoc.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html']
}
html_theme_options = {
    'analytics_anonymize_ip': False,
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_logo = "logo.png"



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
