#!/bin/sh

apt-get update 

# Dependencies
dependencies="python3 \
    python3-pip"

# Required python packages
python_packages="pycrate \
    json2xml
    xmltodict"

# Install dependencies, packages
apt-get install -y $dependencies
pip3 install $python_packages
