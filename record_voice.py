# -*- coding: utf-8 -*-
import sys, select, termios,tty
import os

def getKey():
  fd = sys.stdin.fileno()
  old = termios.tcgetattr(fd)
  new = termios.tcgetattr(fd)
  new[3] &= ~termios.ICANON
  new[3] &= ~termios.ECHO
  try:
      termios.tcsetattr(fd, termios.TCSANOW, new)
      ch = sys.stdin.read(1)

  finally:
      termios.tcsetattr(fd, termios.TCSANOW, old)

  print(ch)
  return ch

def main():
  try:

    while 1:
      key = getKey()
      if key == 'r':
        # record sound
        os.system("arecord -d 5 -f cd 'test.wav'")
        print("finish recording")
      elif key == 'p':
        #play sound
        os.system("aplay 'test.wav'")
      elif key == 'q':
        break
      elif key:
        print(key)

  except( KeyboardInterrupt, SystemExit):
    print( "SIGINTを検知" )

if __name__ == "__main__":
  main()