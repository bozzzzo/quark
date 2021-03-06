# -*- coding: utf-8 -*-
#
# json_assembling documentation build configuration file, created by Quark
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'json_assembling'
copyright = u'2015, json_assembling authors'
author = u'json_assembling authors'
version = '0.0.1'
release = '0.0.1'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'json_assemblingdoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'json_assembling.tex', u'json_assembling Documentation',
     u'json_assembling authors', 'manual'),
]
man_pages = [
    (master_doc, 'json_assembling', u'json_assembling Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'json_assembling', u'json_assembling Documentation',
     author, 'json_assembling', 'One line description of json_assembling.',
     'Miscellaneous'),
]
