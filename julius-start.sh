#!/bin/sh

# julius -C word.jconf -nostrip
#julius -C word.jconf -module > /dev/null &
/usr/local/bin/julius -C /home/pi/src/voice-printer/word.jconf -module > /dev/null &
echo $! #output process id
sleep 3 # [s]