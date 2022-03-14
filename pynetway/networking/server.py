## System Imports
from typing import Callable, List
import logging
import threading


## Application Imports
from pynetway.networking.configuration import ConnectionConfiguration


## Library Imports
import zmq


class Server:
	def __init__(self, connection_configuration: ConnectionConfiguration):
		self.connection_configuration = connection_configuration
		
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.REP)
		
		self.__Bind()
		
		self.receive_thread: threading.Thread
		self.__StartReceive()
		
		self.receivers: List[Callable] = []
	
	def __Bind(self):
		self.socket.bind(self.connection_configuration.ConnectionUrl)
	
	def SendMessage(self, message: bytes):
		self.socket.send(message)
		
		logging.info(f"Sent {message.__sizeof__()} bytes")
		
		self.__StartReceive()
	
	def __StartReceive(self):
		self.receive_thread = threading.Thread(name="ServerMessageReceiveThread", target=self.__Receive, args=())
		self.receive_thread.start()
	
	def __Receive(self):
		while True:
			message = self.socket.recv()
			
			logging.info(f'Received {message.__sizeof__()} bytes')
			
			for receiver in self.receivers:
				receiver(message)
			
			return
	
	def AddReceiver(self, receiver: Callable):
		if receiver not in self.receivers:
			self.receivers.append(receiver)


if __name__ == '__main__':
	config = ConnectionConfiguration(Hostname="127.0.0.1",
	                                 Port=7000,
	                                 Protocol="TCP")
	
	server = Server(config)
