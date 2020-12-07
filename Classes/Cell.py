class Cell:

    def __init__(
        self, north_border,
        east_border, south_border,
        west_border, is_winning_cell
    ):
        self._north_border = north_border
        self._east_border = east_border
        self._south_border = south_border
        self._west_border = west_border
        self.is_winning_cell = is_winning_cell

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

    def walk_into(self):
        return self
