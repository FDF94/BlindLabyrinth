from random import choices


class Cell:

    def __init__(
        self, north_border,
        east_border, south_border,
        west_border, is_winning_cell,
        row, col
    ):
        self._north_border = north_border
        self._east_border = east_border
        self._south_border = south_border
        self._west_border = west_border
        self.is_winning_cell = is_winning_cell
        # This property is useful for creating mazes
        self.is_visited = False
        self.row = row
        self.col = col
        self._has_puddle = choices([True, False], cum_weights=[1, 11])[0]
        self._beeper = None

    def go_in_direction(self, direction):
        actions = {
            "N": self._north_border.walk_into,
            "E": self._east_border.walk_into,
            "S": self._south_border.walk_into,
            "W": self._west_border.walk_into,
        }
        next_cell = actions[direction]()
        if next_cell is not None:
            return next_cell
        else:
            return self

    def knock_in_direction(self, direction):
        actions = {
            "N": self._north_border.knock,
            "E": self._east_border.knock,
            "S": self._south_border.knock,
            "W": self._west_border.knock,
        }
        actions[direction]()

    def knock(self) -> None:
        print("Whoosh!")

    def walk_into(self):
        if self._has_puddle:
            print("Splash!")
        if self._beeper:
            self._beeper.beep()
        return self

    def place_beeper(self, beeper):
        self._beeper = beeper
        self._beeper.subscribe(print("Beep"))
