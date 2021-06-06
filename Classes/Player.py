class Player:

    _cardinal_directions = ("N", "E", "S", "W")
    _relative_directions = ("Forward", "Right", "Backward", "Left")
    _turning_dict = {
        "Left": -1,
        "Right": 1
    }

    def __init__(self, cell, beeper):
        self.current_cell = cell
        self._facing = "N"
        self._beeper = beeper
        self._observers = []

    def turn(self, direction: str) -> None:
        i = self._turning_dict[direction]

        current_index = self._cardinal_directions.index(self._facing)
        self._facing = self._cardinal_directions[
            (current_index + i) % len(self._cardinal_directions)
        ]
        for x in self._observers:
            x.player_event("turn", self._facing)

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
            self._beeper.is_set = True
            self.current_cell.place_beeper(self._beeper)
            self._beeper = None
        else:
            for x in self._observers:
                x.player_event("no_beep")

    def subscribe(self, subscriber):
        self._observers.append(subscriber)
