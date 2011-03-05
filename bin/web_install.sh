#!/bin/bash

# to use this file, run the following command:
# curl -q http://bullseye-code.googlecode.com/svn/trunk/bin/web_install.sh | /bin/bash

VER=0.1.1
cd /tmp
mkdir ~/Desktop/bullseye-code
curl -o /tmp/bullseye.tgz http://bullseye-code.googlecode.com/files/bullseye_code-$VER.tar.gz
tar xvfz bullseye.tgz
cd bullseye_code-$VER
cp -r ./usr ~/Desktop/bullseye-code
echo "Please enter your password to install bullseye-code"
sudo python setup.py install
