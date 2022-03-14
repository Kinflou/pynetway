## System Imports
import inspect
from dataclasses import dataclass, field
from pprint import pprint


## Application Imports


## Library Imports
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True, order=True)
class ConnectionConfiguration:
	
	Hostname: str = field(default="0.0.0.0")
	
	Port: int = field(default=10)
	
	Protocol: str = field(default="tcp")
	
	@property
	def ConnectionUrl(self) -> str:
		return f"{self.Protocol.lower()}://{self.Hostname}:{self.Port}"


if __name__ == '__main__':
	configuration = ConnectionConfiguration()
	
	pprint(inspect.getmembers(ConnectionConfiguration, inspect.isfunction))
	
	breakpoint()
	