## System Imports
from typing import List, Callable
import logging


## Application Imports
from pynetway.networking.configuration import ConnectionConfiguration


## Library Imports
import zmq


class Client:
	def __init__(self, connection_configuration: ConnectionConfiguration):
		self.connection_configuration = connection_configuration
		
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.REQ)
		
		self.alive: bool = False
		
		# TODO: Set a connected flag
		# self.connected: bool =
		
		self.__Connect()
		
		# self.receive_thread = threading.Thread(name="ClientMessageReceiveThread", target=self.__Receive, args=())
		
		self.receivers: List[Callable] = []
	
	def __Connect(self):
		self.socket.connect(self.connection_configuration.ConnectionUrl)
		
		return self.socket
	
	def SendMessage(self, message: bytes):
		self.socket.send(message)
		
		address = str(self.socket.LAST_ENDPOINT)
		
		logging.info(f"Sent {message.__sizeof__()} bytes to {address}")
		
		# self.receive_thread.start()
	
	def ReceiveMessage(self):
		return self.__Receive()
	
	def __Receive(self):
		while True:
			message = self.socket.recv()
			
			logging.info(f'Received {message.__sizeof__()} bytes from {self.socket.underlying.imag}')
			
			for receiver in self.receivers:
				receiver(message)
			
			return message
	
	def AddReceiver(self, receiver: Callable):
		if receiver not in self.receivers:
			self.receivers.append(receiver)
	

if __name__ == '__main__':
	
	config = ConnectionConfiguration(Hostname="127.0.0.1",
	                                 Port=7000,
	                                 Protocol="TCP")
	
	client = Client(config)
	
	breakpoint()
