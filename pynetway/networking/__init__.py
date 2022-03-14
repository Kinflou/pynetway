## System Imports
from enum import Enum


## Application Imports
from pynetway.networking.client import Client
from pynetway.networking.server import Server
from pynetway.networking.configuration import ConnectionConfiguration


## Library Imports
import msgpack


class Direction(Enum):
    Incoming = 0
    Outgoing = 1


if __name__ == '__main__':
    connection_config = ConnectionConfiguration(Hostname="127.0.0.1",
                                                Port=7000,
                                                Protocol="TCP")
    
    server = Server(connection_config)
    client = Client(connection_config)
    
    client.SendMessage(msgpack.packb("Hello"))
    
    breakpoint()
