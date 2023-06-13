import logging
import socket
import time
import os
from threading import *

from Logic.Device import Device
from Logic.Player import Players
from Packets.PiranhaMessage import packets

from Networking.ClientThread import ClientThread


def _(*args):
	print('[SERVER]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()


class ServerThread:
	Clients = {"ClientCounts": 0, "Clients": {}}
	ThreadCount = 0

	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip

	def start(self):
		self.server.bind((self.ip, self.port))
		_(f'Server started! Ip: {self.ip}, Port: {self.port}')
		while True:
			self.server.listen()
			client, address = self.server.accept()
			_(f'New connection! Ip: {address[0]}')
			ClientThread(client, address).start()
			ServerThread.ThreadCount += 1