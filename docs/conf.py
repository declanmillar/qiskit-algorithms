# This code is part of a Qiskit project.
#
# (C) Copyright IBM 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name

"""Sphinx documentation builder."""

# -- General configuration ---------------------------------------------------
import datetime
import doctest

import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("."))

project = "Qiskit Algorithms"
copyright = f"2017-{datetime.date.today().year}, Qiskit Algorithms Development Team" # pylint: disable=redefined-builtin
author = "Qiskit Algorithms Development Team"

# The short X.Y version
version = "0.1"
# The full version, including alpha/beta/rc tags
release = "0.1.0"

# Manually add the gallery CSS file for now
# TODO: Figure out why the styling is not working by default
html_css_files = [
    "nbsphinx-gallery.css",
]

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "reno.sphinxext",
    "sphinx_design",
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.doctest",
    "qiskit_sphinx_theme",
    "nbsphinx"
]

rst_prolog = """
.. raw:: html

    <br><br><br>

.. |version| replace:: {0}
""".format(
    release
)

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}
.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. note::
        This page was generated from `docs/{{ docname }}`__.

        __"""

vers = version.split(".")
link_str = f" https://github.com/qiskit-community/qiskit-algorithms/blob/stable/{vers[0]}.{vers[1]}/docs/"
nbsphinx_prolog += link_str + "{{ docname }}"

nbsphinx_timeout = 360
nbsphinx_execute = os.getenv("QISKIT_DOCS_BUILD_TUTORIALS", "never")
nbsphinx_widgets_path = ""
nbsphinx_thumbnails = {
    "**": "_static/images/logo.png",
}

templates_path = ["_templates"]

# Number figures, tables and code-blocks if they have a caption.
numfig = True
# Available keys are 'figure', 'table', 'code-block' and 'section'.  '%s' is the number.
numfig_format = {"table": "Table %s"}

# The language for content autogenerated by Sphinx or the default for gettext content translation.
language = "en"

# Relative to source directory, affects general discovery, and html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

pygments_style = "colorful"

# Whether module names are included in crossrefs of functions, classes, etc.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
modindex_common_prefix = ["qiskit."]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "qiskit": ("https://qiskit.org/documentation/", None),
}

# -- Options for HTML output -------------------------------------------------

html_theme = "qiskit-ecosystem"
html_last_updated_fmt = "%Y/%m/%d"
html_title = f"{project} {release}"


# -- Options for Autosummary and Autodoc -------------------------------------

# Note that setting autodoc defaults here may not have as much of an effect as you may expect; any
# documentation created by autosummary uses a template file (in autosummary in the templates path),
# which likely overrides the autodoc defaults.

# Move type hints from signatures to the parameter descriptions (except in overload cases, where
# that's not possible).
autodoc_typehints = "description"
# Only add type hints from signature to description body if the parameter has documentation.  The
# return type is always added to the description (if in the signature).
autodoc_typehints_description_target = "documented_params"

autosummary_generate = True
autosummary_generate_overwrite = False
autoclass_content = "both"


# -- Options for Doctest --------------------------------------------------------

doctest_default_flags = (
    doctest.ELLIPSIS
    | doctest.NORMALIZE_WHITESPACE
    | doctest.IGNORE_EXCEPTION_DETAIL
    | doctest.DONT_ACCEPT_TRUE_FOR_1
)

# Leaving this string empty disables testing of doctest blocks from docstrings.
# Doctest blocks are structures like this one:
# >> code
# output
doctest_test_doctest_blocks = ""
