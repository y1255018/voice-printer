#!/bin/sh

# get dictation-kit ver4.5
wget https://osdn.net/projects/julius/downloads/71011/dictation-kit-4.5.zip
unzip dictation-kit-4.5.zip dictation-kit

# install julius ver4.5
sudo apt-get install osspd-alsa libasound2-dev
cd julius
./configure --with-mictype=alsa
make
sudo make install