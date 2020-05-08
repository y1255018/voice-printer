#!/bin/sh

# julius -C word.jconf -nostrip
julius -C word.jconf -module > /dev/null &
echo $! #プロセスIDを出力
sleep 3 #2秒間スリープ