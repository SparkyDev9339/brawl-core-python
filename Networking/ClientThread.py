import logging
import socket
import time
import os
from threading import *

from Logic.Device import Device
from Logic.Player import Players

from Packets.PiranhaMessage import packets
from Logic.PacketsHelper import PacketsHelper

def _(*args):
	print('[CLIENT]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()

class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("Receive Error!")
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)
					packet_name = PacketsHelper.getMessageName(packet_id)

					if packet_id in packets:
						_(f'Packet Sent!. Id: {packet_id}, Lenght: {length}, Name: {packet_name}.')
						message = packets[packet_id](self.client, self.player, data)
						message.decode()
						message.process()

						if packet_id == 10101:
							_('LoginMessage sent!')

					else:
						_(f'Packet not handled! Id: {packet_id}')

				if time.time() - last_packet > 10:
					print(f"[INFO] Ip: {self.address[0]} disconnected!")
					self.client.close()
					break
		except ConnectionAbortedError:
			print(f"[INFO] Ip: {self.address[0]} disconnected!")
			self.client.close()
		except ConnectionResetError:
			print(f"[INFO] Ip: {self.address[0]} disconnected!")
			self.client.close()
		except TimeoutError:
			print(f"[INFO] Ip: {self.address[0]} disconnected!")
			self.client.close()
