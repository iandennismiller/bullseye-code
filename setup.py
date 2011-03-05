#!/usr/bin/env python

# (c) 2011 Ian Dennis Miller
# http://bullseye-code.googlecode.com

import platform, re, sys, os, shutil
from distutils.core import setup

if re.search(r'^Windows', platform.platform()):
    sys.argv[1:] = ['install']
    print "\nPerforming Windows-specific installation"
    c = raw_input("press enter to start...")
    home_path = os.path.expanduser('~')
    install_path = os.path.join(home_path, 'Start Menu', 'Programs', 'Bullseye Code')
    try:
        os.mkdir(install_path)
    except WindowsError:
        pass

    bin_file = os.path.join(os.getcwd(), 'bin', 'bullseye.py')
    shutil.copy(bin_file, install_path)
    print "Installed Bullseye Code to the start menu."

setup(name='bullseye_code',
    version='0.1.2',
    description = "Interactively code raw data according to the bullseye paradigm",
    author = 'Ian Dennis Miller',
    author_email = 'ian@saperea.com',
    url = 'http://bullseye-code.googlecode.com',
    packages=['Bullseye'],
    py_modules=['bottle'],
    long_description= """
    Given raw data containing words arranged within a circular field, this tool provides an 
    interface for (1) coding the words and (2) measuring distance to the center of the field.
    Although this program is controlled through a web browser, the server runs locally, so 
    there is never any need to upload participant data to a remote server.""",
    package_dir = {'': 'lib'},
    scripts=['bin/bullseye.py'],
    license="GPL v2",
    platforms = ["any"],
)

if re.search(r'^Windows', platform.platform()):
    print "\nInstallation successful.  You can now find Bullseye Code in the start menu."
    c = raw_input("press enter to finish...")
