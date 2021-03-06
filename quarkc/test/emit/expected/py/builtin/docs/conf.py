# -*- coding: utf-8 -*-
#
# builtin documentation build configuration file, created by Quark
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'builtin'
copyright = u'2015, builtin authors'
author = u'builtin authors'
version = '0.0.1'
release = '0.0.1'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'builtindoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'builtin.tex', u'builtin Documentation',
     u'builtin authors', 'manual'),
]
man_pages = [
    (master_doc, 'builtin', u'builtin Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'builtin', u'builtin Documentation',
     author, 'builtin', 'One line description of builtin.',
     'Miscellaneous'),
]
