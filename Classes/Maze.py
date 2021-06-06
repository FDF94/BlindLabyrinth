from Classes.Cell import Cell
from Classes.Wall import Wall
from View.View import View
from typing import List, Tuple
from random import choice

CellRow = List[Cell]
CellGrid = List[CellRow]


class Maze():

    def __init__(self, rows: int, columns: int, view: View):
        wall = Wall()
        self.cells_grid = [
            [Cell(wall, wall, wall, wall, False, j, i) for i in range(rows)]
            for j in range(columns)
        ]
        self.cells_grid[0][0].is_winning_cell = True
        self._max_x = rows - 1
        self._max_y = columns - 1

        # Events subscription
        # ToDo this should definitely not be here
        wall.knock_event += view.knock_event
        wall.walk_into_event += view.walk_into_event
        for row in self.cells_grid:
            for cell in row:
                cell.puddle_event += view.puddle_event
                cell.whoosh_event += view.whoosh_event

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

    def generate_maze(self, cells_grid):
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

    def break_down_wall(self, first_cell, second_cell):
        x1 = first_cell.row
        y1 = first_cell.col
        x2 = second_cell.row
        y2 = second_cell.col

        row_dif = x2 - x1
        col_dif = y2 - y1

        # ToDo: refactor to avoid using modifying private
        # properties

        if col_dif == 1:
            first_cell._borders["E"] = second_cell
            second_cell._borders["W"] = first_cell
        elif col_dif == -1:
            first_cell._borders["W"] = second_cell
            second_cell._borders["E"] = first_cell
        elif row_dif == 1:
            first_cell._borders["S"] = second_cell
            second_cell._borders["N"] = first_cell
        elif row_dif == -1:
            first_cell._borders["N"] = second_cell
            second_cell._borders["S"] = first_cell
