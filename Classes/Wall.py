from Classes.Event import Event
from Classes.CellLimit import CellLimit


class Wall(CellLimit):

    def __init__(self):
        self.walk_into_event = Event()
        self.knock_event = Event()

    def walk_into(self) -> None:
        self.walk_into_event.notify()

    def knock(self) -> None:
        self.knock_event.notify()
