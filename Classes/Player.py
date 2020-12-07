class Player:

    _cardinal_directions = ("N", "E", "S", "W")
    _relative_directions = ("Forward", "Right", "Backward", "Left")

    def __init__(self, cell):
        self.current_cell = cell
        self._facing = "N"

    def turn(self, direction):
        turning_dict = {
            "Left": -1,
            "Right": 1
        }
        i = turning_dict[direction]

        current_index = self._cardinal_directions.index(self._facing)
        self._facing = self._cardinal_directions[
            (current_index + i) % len(self._cardinal_directions)
        ]
        print(f"Now facing {self._facing}")

    def go_in_direction(self, direction):
        direction_index = self._relative_directions.index(direction)
        current_cardinal_index = self._cardinal_directions.index(self._facing)
        cardinal_index = (direction_index + current_cardinal_index) % 4
        self.current_cell = self.current_cell.go_in_direction(
            self._cardinal_directions[cardinal_index]
        )
