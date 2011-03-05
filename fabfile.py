from fabric.api import local
import os

def sdist():
    print local('cp wiki/ReadMe.wiki doc/README.txt')
    #print local('cp wiki/InstallWindows.wiki doc/INSTALL-WIN.TXT')
    #print local('cp wiki/InstallUnix.wiki doc/INSTALL-UNIX.TXT')
    print local('rm -rf build; python setup.py sdist --formats=zip,gztar')

def tag():
    ver = local('python setup.py --version').rstrip()
    cmd = 'svn cp https://bullseye-code.googlecode.com/svn/trunk/ https://bullseye-code.googlecode.com/svn/tags/%s/'
    os.system(cmd % ver)

def test():
    cmd = 'nosetests -v t/test_fft_data.py'
    os.system(cmd)
