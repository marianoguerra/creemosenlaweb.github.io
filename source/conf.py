#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Creemos en la Web documentation build configuration file, created by
# sphinx-quickstart on Sun Apr 22 17:11:56 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append(os.path.join(os.path.abspath('..'), 'themes', 'sphinxbootstrap4theme'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Creemos en la Web'
copyright = '2018, Lara Garbero Tais, Mariano Guerra'
author = 'Lara Garbero Tais, Mariano Guerra'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
# see Makefile's setup target
import sphinxbootstrap4theme

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinxbootstrap4theme'
html_theme_path = [sphinxbootstrap4theme.get_path()]

html_theme_options = {
    # Navbar style.
    # Values: 'fixed-top', 'full' (Default: 'fixed-top')
    'navbar_style' : 'fixed-top',

    # Navbar link color modifier class.
    # Values: 'dark', 'light' (Default: 'dark')
    'navbar_color_class' : 'dark',

    # Navbar background color class.
    # Values: 'inverse', 'primary', 'faded', 'success',
    #         'info', 'warning', 'danger' (Default: 'inverse')
    'navbar_bg_class' : 'inverse',

    # Show global TOC in navbar.
    # To display up to 4 tier in the drop-down menu.
    # Values: True, False (Default: True)
    'navbar_show_pages' : False,

    # Link name for global TOC in navbar.
    # (Default: 'Pages')
    'navbar_pages_title' : 'Pages',

    # Specify a list of menu in navbar.
    # Tuples forms:
    #  ('Name', 'external url or path of pages in the document', boolean)
    # Third argument:
    # True indicates an external link.
    # False indicates path of pages in the document.
    'navbar_links' : [
         ('Home', 'index', False),
         #("Link", "http://example.com", True)
    ],

    # Total width(%) of the document and the sidebar.
    # (Default: 80%)
    'main_width' : '80%',

    # Render sidebar.
    # Values: True, False (Default: True)
    'show_sidebar' : False,

    # Render sidebar in the right of the document.
    # Values：True, False (Default: False)
    'sidebar_right': False,

    # Fix sidebar.
    # Values: True, False (Default: True)
    'sidebar_fixed': True,

    # Html table header class.
    # Values: 'inverse', 'light' (Deafult: 'inverse')
    'table_thead_class' : 'inverse'
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'css/custom.css']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'CreemosenlaWebdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'CreemosenlaWeb.tex', 'Creemos en la Web Documentation',
     'Lara Garbero Tais, Mariano Guerra', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'creemosenlaweb', 'Creemos en la Web Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'CreemosenlaWeb', 'Creemos en la Web Documentation',
     author, 'CreemosenlaWeb', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

def setup(app):
    app.add_stylesheet('css/custom.css')
