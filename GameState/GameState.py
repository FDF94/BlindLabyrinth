from GameEntities.Cell import Cell
from GameEntities.Wall import Wall
from GameEntities.Player import Player
from GameEntities.Maze import Maze
from Infrastructure.Sound import Sound
from Infrastructure.Event import Event
from GameState.CardinalDirections import CardinalDirections as CD


class GameState:

    def __init__(self, player: Player, maze: Maze):
        self._player = player
        self._maze = maze
        self.is_won = False

        # Events
        self.win_event = Event()
        self.sound_event = Event()
        self.puddle_event = Event()
        self.whoosh_event = Event()
        self.knock_event = Event()
        self.walk_into_event = Event()

        # Events subscription
        self._maze.wall.knock_event += self.knock_event.notify
        self._maze.wall.walk_into_event += self.walk_into_event.notify
        for row in self._maze.cells_grid:
            for cell in row:
                cell.puddle_event += self.puddle_event.notify
                cell.whoosh_event += self.whoosh_event.notify

    def set_game_as_won(self):
        self.is_won = True
        self.win_event.notify()

    def beep_event(self, beeper_row: int, beeper_col: int):
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
        return type(cell.borders[relative_direction]) == Wall

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
            (1, 0): CD.SOUTH,
            (-1, 0): CD.NORTH,
            (0, -1): CD.WEST,
            (0, 1): CD.EAST,
        }
        try:
            return results[dif]
        except KeyError:
            return None
