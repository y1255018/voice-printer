#!/bin/sh

# record
arecord -d 10 -f cd test.wav

#play
aplay test.wav