import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = 'DisOAuth2'
copyright = '2023, Arcader717'
author = 'Arcader717'
version = '1.4'
release = '1.4.0'

extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
  'sphinx_click'
]
excludes_patterns = []
html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
  "source_repository": "https://github.com/Arcader717/Async-DisOAuth2",
  "announcement": "DisOAuth will be renamed to discoauth after the 2.0 update"
}
