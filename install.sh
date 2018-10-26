#!/usr/bin/env bash

echo "Note: need \"sudo\""
sleep 1

apt-get install portaudio19-dev
apt-get install python3
apt-get install python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install webob

export LC_ALL=C                 # for pip

git submodule update --init
cd anki-bundled || exit 1
python3 -m pip install -r requirements.txt
