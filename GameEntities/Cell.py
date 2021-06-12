from random import choices
from Infrastructure.Event import Event
from GameEntities.CellLimit import CellLimit
from GameState.CardinalDirections import CardinalDirections as CD


class Cell(CellLimit):

    def __init__(
        self, north_border: CellLimit,
        east_border: CellLimit, south_border: CellLimit,
        west_border: CellLimit, is_winning_cell: CellLimit,
        row: int, col: int
    ):
        self.borders = {
            CD.NORTH: north_border,
            CD.SOUTH: south_border,
            CD.EAST: east_border,
            CD.WEST: west_border,
        }
        self.is_winning_cell = is_winning_cell
        # This property is useful for creating mazes
        self.is_visited = False
        self.row = row
        self.col = col
        self._has_puddle = choices([True, False], cum_weights=[1, 11])[0]

        # Events
        self.puddle_event = Event()
        self.whoosh_event = Event()

    def go_in_direction(self, direction):

        next_cell = self._borders[direction].walk_into()
        if next_cell is not None:
            return next_cell
        else:
            return self

    def knock_in_direction(self, direction):
        self._borders[direction].knock()

    def knock(self) -> None:
        self.whoosh_event.notify()

    def walk_into(self):
        if self._has_puddle:
            self.puddle_event.notify()

        return self
