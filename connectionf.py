from abc import ABC, abstractmethod
from socketc import SocketC

class ConnectionF(ABC):
    @abstractmethod
    def create_socket(self):
        pass