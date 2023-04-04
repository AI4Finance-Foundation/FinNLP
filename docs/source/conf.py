# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# change path
import sys, os
sys.path.insert(0, os.path.abspath("../../../finnlp/"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FinNLP'
copyright = '2023, AI4Finance Foundation'
author = 'Oliver Wang, Xiao-yang Liu'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark','sphinx_markdown_tables',
    # "myst_parser",                                                     # Markdown Support
    'myst_nb',                                                         # Jupyter Notebook
    'sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc',    # Codes
              ]
todo_include_todos = True
templates_path = ['_templates']
exclude_patterns = []

language = '[en, zh_CN]'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

#编辑配置文件source/conf.py在最后一行复制下方配置
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'markdown',
#     '.md': 'markdown',
# }

# myst_enable_extensions = [
#     "amsmath",
#     "attrs_inline",
#     "colon_fence",
#     "deflist",
#     "dollarmath",
#     "fieldlist",
#     "html_admonition",
#     "html_image",
#     "linkify",
#     "replacements",
#     "smartquotes",
#     "strikethrough",
#     "substitution",
#     "tasklist",
# ]