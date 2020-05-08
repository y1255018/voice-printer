#!/bin/sh

#音素データにコンパイル
iconv ./word.yomi | yomi2voca.pl > ./word.dic