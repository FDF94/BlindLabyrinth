from Classes.Player import Player
from Classes.Maze import Maze
from Classes.Counter import Counter
from Classes.Beeper import Beeper
from HardwareControl.helper_functions import handle_input

movements = {
    "E": lambda x: x.turn("Right"),
    "Q": lambda x: x.turn("Left"),
    "W": lambda x: x.go_in_direction("Forward"),
    "A": lambda x: x.go_in_direction("Left"),
    "S": lambda x: x.go_in_direction("Backward"),
    "D": lambda x: x.go_in_direction("Right"),
    "J": lambda x: x.knock_in_direction("Left"),
    "L": lambda x: x.knock_in_direction("Right"),
    "B": lambda x: x.set_beeper(),
    "": lambda x: print("Standing here, doing nothing")
}


def main():
    # Initialize all objects
    counter = Counter()
    beeper = Beeper()
    maze = Maze(3, 3)
    origin_cell = maze.cells_grid[-1][-1]
    player = Player(origin_cell, beeper)
    winning_cell = False

    # Make subscriptions
    counter.subscribe(beeper)
    print("\nBegin!")

    while not winning_cell:
        counter.tick()
        movement = handle_input()
        movements[movement](player)
        winning_cell = player.current_cell.is_winning_cell

    print("Congrats! You win!")


if __name__ == "__main__":
    main()
