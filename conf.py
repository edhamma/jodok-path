# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'The Path to Nibbana'
copyright = 'XXX'
author = 'Phra Dhamma Therrarach Mahamuni (Jodok)'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
try:
    import subprocess
    release=subprocess.check_output(['git','rev-parse','--short','HEAD']).strip().decode('utf-8')
except subprocess.CalledProcessError:
    release = '[built-outside-git]'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.fulltoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'github_user':'edhamma',
    'github_repo':'jodook-path',
    'github_banner':'true',
    # 'fixed_sidebar':'true',
    # 'sidebar_collapse':'true',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'JodokPath'


# -- Options for LaTeX output ------------------------------------------------

latex_maketitle=r'''
\makeatletter%
\hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
\makeatother%
\begin{titlepage}%
    \vspace*{\baselineskip}
    \vfill
    \hbox{%
        \hspace*{0.15\textwidth}%
        \rule{1pt}{.95\textheight}
        \hspace*{0.05\textwidth}%
        \parbox[b]{0.8\textwidth}{
            \vbox to.95\textheight{%
                \vspace{.05\textheight}
                {\noindent\Huge\bfseries The Path\\[0.5\baselineskip]
                to Nibbāna}\\[4\baselineskip]
                {\Large\emph{Phra Dhamma Theerarach Mahamuni \\ (Ajahn Jodok)}}\par
                \vfill % space{0.3\textheight}
                Other formats (PDF, HTML, ePub, …) available from \href{https://github.com/edhamma/jodok-path}{github.com/edhamma/jodok-path}.
                \\[\baselineskip]
                {\noindent This e-book is a community effort. If you spot an error in the text (such as misspelled word), go to the address above and report or (if you have the skill) fix it. Thanks!}
                \\[\baselineskip]
                {\noindent Revision \releasename, built \today.}
            }% end of vbox
        }% end of parbox
    }% end of hbox
    \vfill
\end{titlepage}
'''

latex_engine='lualatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'releasename':release,
    'papersize': 'a5paper',

    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \usepackage{emptypage}
        \usepackage{titling}
        \makeatletter
        \fancypagestyle{normal}{
          \fancyhf{}
          \fancyfoot[LE,RO]{\thepage}
          \fancyfoot[RE,LO]{}
          \fancyhead[RE]{\releasename}
          \fancyhead[LE]{\@title}
          \fancyhead[RO]{\emph{\leftmark}}
          \renewcommand{\headrulewidth}{0.4pt}
          \renewcommand{\footrulewidth}{0pt}
        }
        \fancypagestyle{plain}{
          \renewcommand{\footrulewidth}{0pt}
          \fancyhead{}
          \renewcommand{\headrulewidth}{0pt}
        }
        \setotherlanguage{thai}
        \makeatother
        % \renewcommand{\chaptermark}[1]{\markboth{#1}{}}
        \usepackage[numbered]{bookmark}
        \iffalse  \let\frontmatter\relax \let\mainmatter\relax \let\backmatter\relax \fi
    ''',
    'fncychap':'',
    'sphinxsetup':r'''
        HeaderFamily=\bfseries,
        TitleColor={rgb}{0,0,0},
        InnerLinkColor={rgb}{0,0,0},
        hmargin={1.5cm,2cm},
        vmargin={2cm,2cm},
    ''',
    'fontpkg':r'\usepackage{fontspec}\setmainfont{TeX Gyre Pagella}',
    'maketitle':latex_maketitle,

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'JodokPath.tex', 'The Path to Nibbāna',
     'Phra Dhamma Theerarach Mahamuni (Jodok)', 'book'),
]
latex_toplevel_sectioning='chapter'


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'jodok-path', 'The Path to Nibbāna',
     [author], 1)
] 


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'JodokPath', 'The Path to Nibbāna',
     author, 'JodokPath', '',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------


# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = ''
epub_copyright = copyright
epub_cover = ('_static/cover.jpg','epub-cover.html')
epub_language='en'
epub_basename='jodok-path-to-nibbana'
epub_use_index=False
epub_scheme='ISBN'
epub_identifier = ''
# A unique identification for the text.
epub_uid = 'jodok-path-to-nibbana'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
