#!/bin/bash

# to use this file, run the following command:
# curl -s http://bullseye-code.googlecode.com/svn/trunk/bin/web_install.sh | /bin/bash

VER=0.1.1
cd /tmp
if [ -d ~/Desktop/bullseye-code ]
	echo "~/Desktop/bullseye-code already exists; I don't want to overwrite it"
	exit 1
fi
mkdir ~/Desktop/bullseye-code
curl -s -o /tmp/bullseye.tgz http://bullseye-code.googlecode.com/files/bullseye_code-$VER.tar.gz
tar xvfz bullseye.tgz
rm bullseye.tgz
cd bullseye_code-$VER
cp -r ./usr ~/Desktop/bullseye-code
echo "Please enter your password to install bullseye-code"
python setup.py build
sudo python setup.py install
rm -rf /tmp/bullseye_code-$VER
