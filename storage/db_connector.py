from abc import ABC, abstractmethod


class DBConnector(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def create_database(self):
        # if not exist
        # error if exist
        pass

    @abstractmethod
    def create_table(self):
        # if not exist
        pass
