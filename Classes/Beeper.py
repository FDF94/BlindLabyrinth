from Classes.Event import Event
from Classes.Cell import Cell


class Beeper:

    def __init__(self):
        self.beep_event = Event()
        self.beeper_set_event = Event()
        self._is_set = False
        self._cell = None

    def count(self, count: int):
        if(count % 5 == 0 and self._is_set):
            self.beep_event.notify(self._cell.row, self._cell.col)

    def set_beeper(self, cell: Cell):
        self._is_set = True
        self._cell = cell
        self.beeper_set_event.notify()
