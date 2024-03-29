"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['test.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

# Hack
import sys
import os
if 'py2app' in sys.argv:
    import shutil
    if not os.path.exists('dist/test.app/Contents/Resources/qt_menu.nib'):
        print "Copying missing qt_menu.nib"
        shutil.copytree('qt_menu.nib', 'dist/test.app/Contents/Resources/qt_menu.nib')
