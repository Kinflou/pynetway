## System Imports
import logging


## Application Imports


## Library Imports


logs_directory: str = "logs/"


def Initialize():
	Setup()


def Setup():
	logging.basicConfig(level=logging.INFO,
	                    format="%(asctime)s: %(levelname)s: %(message)s")

