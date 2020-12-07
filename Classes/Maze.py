from Classes.Cell import Cell
from Classes.Wall import Wall
from typing import List
from random import choice

CellRow = List[Cell]
CellGrid = List[CellRow]


class Maze():

    def __init__(self, rows: int, columns: int):
        wall = Wall()
        self.cells_grid = [
            [Cell(wall, wall, wall, wall, False) for i in range(rows)]
            for j in range(columns)
        ]
        self.cells_grid[-1][-1].is_winning_cell = True
        self.generate_maze(self.cells_grid)

    def _is_any_cell_unvisited(self, cells_grid: CellGrid) -> bool:
        for row in cells_grid:
            for cell in row:
                if not cell.is_visited:
                    return True
        return False

    def _get_next_block_coordinates(
        self, selected_direction: str,
        x, y, max_x_value, max_y_value
    ):
        functions_dict = {
            "U": (x, y-1),
            "D": (x, y+1),
            "L": (x-1, y),
            "R": (x+1, y),
        }

        result = functions_dict[selected_direction]
        checks = [
            result[0] < 0,
            result[0] > max_x_value,
            result[1] < 0,
            result[1] > max_y_value]

        if any(checks):
            raise ValueError("Direction is off limits")

        return result

    def find_next_cell(self, cells_grid, x, y, max_x, max_y):
        directions = ["U", "D", "L", "R"]
        is_next_cell_visited = True
        while directions and is_next_cell_visited:
            try:
                selected_direction = choice(directions)
                print(selected_direction)
                next_x, next_y = self._get_next_block_coordinates(
                    selected_direction, x, y, max_x, max_y
                )
                next_cell = cells_grid[next_x][next_y]
                if next_cell.is_visited:
                    directions.pop(directions.index(selected_direction))
                    continue
                is_next_cell_visited = False
                next_cell.is_visited = True
            except ValueError:
                directions.pop(directions.index(selected_direction))

        if directions:
            return (next_x, next_y)
        else:
            return None, None

    def generate_maze(self, cells_grid):
        max_x = len(cells_grid) - 1
        max_y = len(cells_grid[0]) - 1
        current_cell = cells_grid[0][0]
        backtrace = [(0, 0)]
        x = 0
        y = 0

        while True:
            current_cell.is_visited = True
            next_x, next_y = self.find_next_cell(
                cells_grid, x, y, max_x, max_y
            )

            if next_x:
                next_cell = cells_grid[next_x][next_y]
                next_cell.is_visited = True
                self.break_down_wall(cells_grid, x, y, next_x, next_y)
                x = next_x
                y = next_y
                backtrace.append((x, y))
            elif backtrace:
                x, y = backtrace.pop()
            elif not backtrace:
                break

    def break_down_wall(self, cells_grid, x1, y1, x2, y2):
        row_dif = x2 - x1
        col_dif = y2 - y1

        if row_dif == 1:
            cells_grid[x1][y1]._east_border = cells_grid[x2][y2]
            cells_grid[x2][y2]._west_border = cells_grid[x1][y1]
        elif row_dif == -1:
            cells_grid[x1][y1]._west_border = cells_grid[x2][y2]
            cells_grid[x2][y2]._east_border = cells_grid[x1][y1]
        elif col_dif == 1:
            cells_grid[x1][y1]._south_border = cells_grid[x2][y2]
            cells_grid[x2][y2]._north_border = cells_grid[x1][y1]
        elif col_dif == -1:
            cells_grid[x1][y1]._north_border = cells_grid[x2][y2]
            cells_grid[x2][y2]._south_border = cells_grid[x1][y1]
