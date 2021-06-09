from Classes.Event import Event
from Classes.Cell import Cell
from Classes.Beeper import Beeper
from GameState.CardinalDirections import CardinalDirections as CD


class Player:

    _cardinal_directions = (CD.NORTH, CD.EAST, CD.SOUTH, CD.WEST)
    _relative_directions = ("Forward", "Right", "Backward", "Left")
    _turning_dict = {
        "Left": -1,
        "Right": 1
    }

    def __init__(self, cell: Cell, beeper: Beeper):
        self.current_cell = cell
        self._facing = CD.NORTH
        self._beeper = beeper

        # Events
        self.turn_event = Event()
        self.no_beeper_event = Event()

    def turn(self, direction: str) -> None:
        i = self._turning_dict[direction]

        current_index = self._cardinal_directions.index(self._facing)
        self._facing = self._cardinal_directions[
            (current_index + i) % len(self._cardinal_directions)
        ]
        self.turn_event.notify(self._facing)

    def go_in_direction(self, direction: str) -> None:
        direction_index = self._relative_directions.index(direction)
        current_cardinal_index = self._cardinal_directions.index(self._facing)
        cardinal_index = (direction_index + current_cardinal_index) % 4

        self.current_cell = self.current_cell.go_in_direction(
            self._cardinal_directions[cardinal_index]
        )

    def knock_in_direction(self, direction: str) -> None:
        direction_index = self._relative_directions.index(direction)
        current_cardinal_index = self._cardinal_directions.index(self._facing)
        cardinal_index = (direction_index + current_cardinal_index) % 4

        self.current_cell.knock_in_direction(
            self._cardinal_directions[cardinal_index]
        )

    def set_beeper(self):
        if self._beeper:
            self._beeper.set_beeper(self.current_cell)
            self._beeper = None
        else:
            self.no_beeper_event.notify()
