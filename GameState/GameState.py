from Classes.Cell import Cell
from Classes.Wall import Wall
from Classes.Event import Event
from Classes.Player import Player
from Classes.Maze import Maze
from Classes.Sound import Sound


class GameState:

    def __init__(self, player: Player, maze: Maze):
        self._player = player
        self._maze = maze
        self.is_won = False
        self.win_event = Event()
        self.sound_event = Event()

    def set_game_as_won(self):
        self.is_won = True
        self.win_event.notify()

    def beep_event(self, beeper_row, beeper_col):
        relative_direction = self._get_relative_direction(
            self._player.current_cell.row,
            self._player.current_cell.col,
            beeper_row,
            beeper_col
        )
        if relative_direction is not None:
            if relative_direction == "your place":
                is_muffled = False
            else:
                is_muffled = self._is_wall(
                    self._player.current_cell,
                    relative_direction)
            self.sound_event.notify(
                Sound("Beep", relative_direction,
                      is_muffled)
            )

    def _is_wall(self, cell: Cell, relative_direction: str):
        # ToDo refactor to not check private member
        return type(cell._borders[relative_direction]) == Wall

    def _get_relative_direction(
            self,
            first_row: int,
            first_col: int,
            second_row: int,
            second_col: int):
        """
        Returns relative position of the second object
        relative to the first one, as long as they are
        adjacent. Diagonal cells are not considered
        adjacent. If they are not adjacent, returns None
        """
        dif = (second_row - first_row, second_col - first_col)
        results = {
            (0, 0): "your place",
            (1, 0): "S",
            (-1, 0): "N",
            (0, -1): "W",
            (0, 1): "E",
        }
        try:
            return results[dif]
        except KeyError:
            return None