class Player:

    _directions = ("N", "E", "S", "W")

    def __init__(self, cell):
        self._cell = cell
        self._facing = "N"

    def turn_right(self):
        current_index = self._directions.index(self._facing)
        self._facing = self._directions[(current_index + 1) %
                                        len(self._directions)]

    def turn_left(self):
        current_index = self._directions.index(self._facing)
        self._facing = self._directions[(current_index - 1) %
                                        len(self._directions)]
