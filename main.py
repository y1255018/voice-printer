# -*- coding: utf-8 -*-
import socket
import codecs
import serial
from datetime import datetime
import os
import subprocess
import time

class Order:
    def __init__(self):
        self.file = '/home/pi/src/voice-printer/order.txt'
        self.number = 0
        self.status = 0
        self.f_order = ""


    def openOrder(self):
        self.f_order = open(self.file,'w+')
        self.status = 1

    def closeOrder(self):
        if self.status == 1:
          self.f_order.close()

          s = os.path.getsize(self.file)
          if s>0:
            self.printOrder()

          self.status = 0

    def writeOrder(self, text):
        if self.status == 1:
            self.f_order.write(text + "\n")

    def printOrder(self):
        date = datetime.today().strftime("%Y年%m月%d日 %H:%M")
        ser.write(date)
        ser.write("\r")
        ser.write("受付番号: " + str(self.number) + "\r")

        f = open(self.file)
        lines = f.readlines()
        f.close()
        for line in lines:
            ser.write(line)
            ser.write("\r")
        
        ser.write("-----------------------------\r")
        #ser.write("\r\r\r\r\r\r");  # Line Feed
        self.number += 1

order = Order()
ser = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = 2)
   
def main():
  host = '127.0.0.1'
  port = 10500

  p = subprocess.Popen(["/home/pi/src/voice-printer/julius-start.sh"], stdout=subprocess.PIPE, shell=True) # start julius
  pid = str(p.stdout.read().decode('utf-8')) # get julius process ID

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  data=''
  try:
    while(1):
      if '</RECOGOUT>\n.' in data:
        text=''
        cm=''
        for line in data.split('\n'):
          #print(line)
          index = line.find('WORD="')
          index2 = line.find('CM="')
          if index != -1 and index2!=-1:
            text = line[index+6:line.find('"',index+6)]
            cm = line[index2+4:line.find('"',index2+4)]
            score = float(cm)
            
            print(text + " score=" + cm)  

            if score>=1.0:
              if text == '注文開始':
                  os.system("aplay '/home/pi/src/voice-printer/start.wav'")
                  order.openOrder()
              elif text == '注文終了':
                  order.closeOrder()
              else:
                  order.writeOrder(text)

        data=''
      else:
        data=data + str(client.recv(1024))

  except KeyboardInterrupt:
    print("KeyboardInterrupt occured.")
    p.kill()
    subprocess.call(["kill " + pid], shell=True)  # kill julius
    client.close()

if __name__ == "__main__":
  main()