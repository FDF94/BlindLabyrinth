from GameEntities.Cell import Cell
from GameEntities.Wall import Wall
from typing import List, Tuple
from random import choice
from GameState.CardinalDirections import CardinalDirections as CD

CellRow = List[Cell]
CellGrid = List[CellRow]


class Maze():

    def __init__(self, rows: int, columns: int):
        self.wall = Wall()
        self.cells_grid = [
            [Cell(self.wall, self.wall, self.wall, self.wall, False, j, i)
                for i in range(rows)]
            for j in range(columns)
        ]
        self.cells_grid[0][0].is_winning_cell = True
        self._max_x = rows - 1
        self._max_y = columns - 1

        self.generate_maze(self.cells_grid)

    def _is_any_cell_unvisited(self, cells_grid: CellGrid) -> bool:
        for row in cells_grid:
            for cell in row:
                if not cell.is_visited:
                    return True
        return False

    def _get_next_cell_coordinates(
        self, selected_direction: str, cell: Cell
    ) -> Tuple[int, int]:
        x = cell.row
        y = cell.col
        functions_dict = {
            "U": (x-1, y),
            "D": (x+1, y),
            "L": (x, y-1),
            "R": (x, y+1),
        }

        result = functions_dict[selected_direction]
        checks = [
            result[0] < 0,
            result[0] > self._max_y,
            result[1] < 0,
            result[1] > self._max_x
        ]

        if any(checks):
            raise ValueError("Direction is off limits")

        return result

    def find_next_cell(self, cells_grid: CellGrid, current_cell: Cell) -> Cell:
        directions = ["U", "D", "L", "R"]
        is_next_cell_visited = True
        while directions and is_next_cell_visited:
            try:
                selected_direction = choice(directions)
                next_x, next_y = self._get_next_cell_coordinates(
                    selected_direction, current_cell)
                next_cell = cells_grid[next_x][next_y]
                if next_cell.is_visited:
                    directions.pop(directions.index(selected_direction))
                    continue
                is_next_cell_visited = False
                next_cell.is_visited = True
            except ValueError:
                directions.pop(directions.index(selected_direction))

        if directions:
            return next_cell
        else:
            return None

    def generate_maze(self, cells_grid: CellGrid):
        current_cell = cells_grid[0][0]
        backtrace = [current_cell]

        while True:
            current_cell.is_visited = True
            next_cell = self.find_next_cell(cells_grid, current_cell)

            if next_cell:
                next_cell.is_visited = True
                self.break_down_wall(current_cell, next_cell)
                current_cell = next_cell
                backtrace.append(next_cell)
            elif backtrace:
                current_cell = backtrace.pop()
            elif not backtrace:
                break

    def break_down_wall(self, first_cell: Cell, second_cell: Cell):
        x1 = first_cell.row
        y1 = first_cell.col
        x2 = second_cell.row
        y2 = second_cell.col

        row_dif = x2 - x1
        col_dif = y2 - y1

        if col_dif == 1:
            first_cell.borders[CD.EAST] = second_cell
            second_cell.borders[CD.WEST] = first_cell
        elif col_dif == -1:
            first_cell.borders[CD.WEST] = second_cell
            second_cell.borders[CD.EAST] = first_cell
        elif row_dif == 1:
            first_cell.borders[CD.SOUTH] = second_cell
            second_cell.borders[CD.NORTH] = first_cell
        elif row_dif == -1:
            first_cell.borders[CD.NORTH] = second_cell
            second_cell.borders[CD.SOUTH] = first_cell
