#!/bin/bash

# to use this file, run the following command:
# curl -s http://bullseye-code.googlecode.com/svn/trunk/bin/web_install.sh | /bin/bash

VER=`curl -s http://code.google.com/p/bullseye-code/downloads/list | awk \
  '/files\/bullseye_code.*.tar.gz/ {sub(/.tar.gz\"/,""); split($2,a,"-"); print a[3]}'`

echo; echo "0. Begin installation.  Autodetected current version: $VER"

if [ -d ~/Desktop/bullseye-code ]; then
	echo "Error: ~/Desktop/bullseye-code already exists."
	echo "I don't want to overwrite it, since you might have data in it."
	exit 1
fi
mkdir ~/Desktop/bullseye-code

echo; echo "1. Downloading current version of bullseye-code"
curl -s -o /tmp/bullseye.tgz http://bullseye-code.googlecode.com/files/bullseye_code-$VER.tar.gz

echo; echo "2. Extracting bullseye-code into /tmp"
cd /tmp
tar xvfz bullseye.tgz

echo; echo "3. Building bullseye-code"
cd bullseye_code-$VER
python setup.py build

echo; echo "4. If you are asked, please enter your password to install bullseye-code"
sudo python setup.py install
cp -r ./usr ~/Desktop/bullseye-code

echo; echo "5. Removing temporary files"
rm /tmp/bullseye.tgz
rm -rf /tmp/bullseye_code-$VER

echo; echo "6. bullseye-code is successfully installed."
open "http://code.google.com/p/bullseye-code/wiki/ReadMe"
