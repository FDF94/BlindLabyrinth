from abc import ABC, abstractmethod


class CellLimit(ABC):

    @abstractmethod
    def walk_into(self):
        pass

    @abstractmethod
    def knock(self):
        pass
