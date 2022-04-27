from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create_serialize(self):
        pass