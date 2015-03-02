#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Setup.py for Python Wheels, as Generic as possible."""


import os

from setuptools import setup

try:
    from pypandoc import convert
except ImportError:
    convert = None


MODULE_PATH = os.path.join(os.getcwd(), "css-html-js-minify.py")


def find_this(search, filename=MODULE_PATH):
    """Take a string and a filename path string and return the found value."""
    if not search:
        return
    for line in open(str(filename)).readlines():
        if search in line:
            line = line.split("=")[1].strip()
            if "'" in line or '"' in line or '"""' in line:
                line = line.replace("'", "").replace('"', '').replace('"""', '')
            return line


def github_markdown_to_restructuredtext(filename='README.md'):
    """Convert github markdown to restructured text on the fly."""
    if convert:
        restructured_text = convert(filename, 'rst',
                                    format='md', encoding="utf-8")
    else:
        with open(filename) as github_markdown:
            restructured_text = github_markdown.read().strip()
    return restructured_text


setup(

    name="css-html-js-minify",
    version=find_this("__version__"),

    description=("StandAlone Async single-file cross-platform no-dependencies"
                 " Unicode-ready Python3-ready Minifier for the Web."),
    long_description=github_markdown_to_restructuredtext(),

    url=find_this("__url__"),
    license=find_this("__license__"),

    author=find_this("__author__"),
    author_email=find_this("__email__"),
    maintainer=find_this("__author__"),
    maintainer_email=find_this("__email__"),

    include_package_data=True,
    zip_safe=True,
    install_requires=['pip'],
    requires=['pip'],

    scripts=["css-html-js-minify.py"],
    entry_points = {
        'console_scripts': ['css-html-js-minify = css_html_js_minify']
    },

    keywords=['CSS', 'HTML', 'JS', 'Compressor', 'CSS3', 'HTML5', 'Web',
              'Javascript', 'Minifier', 'Minify', 'Uglify', 'Obfuscator',
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',

        'Natural Language :: English',

        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
