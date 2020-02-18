from abc import ABC, abstractmethod


class DBConnector(ABC):

    @abstractmethod
    def connect(self):
        pass
