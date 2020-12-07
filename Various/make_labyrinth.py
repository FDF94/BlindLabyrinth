from Classes.Wall import Wall
from Classes.Cell import Cell


def make_labyinth():
    wall = Wall()
    aux_cell = None
    winning_cell = Cell(
        wall, wall, wall, aux_cell, True
    )

    second_cell = Cell(
        wall, winning_cell, aux_cell, wall, False
    )
    winning_cell._east_border = second_cell

    third_cell = Cell(
        second_cell, wall, aux_cell, wall, False
    )
    second_cell._south_border = third_cell

    origin_cell = Cell(
        third_cell, wall, wall, wall, False
    )
    third_cell._south_border = origin_cell

    return origin_cell
