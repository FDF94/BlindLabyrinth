from Classes.Player import Player
from Various.make_labyrinth import make_labyinth
import getch

movements = {
    "E": lambda x: x.turn("Right"),
    "Q": lambda x: x.turn("Left"),
    "W": lambda x: x.go_in_direction("Forward"),
    "A": lambda x: x.go_in_direction("Left"),
    "S": lambda x: x.go_in_direction("Backward"),
    "D": lambda x: x.go_in_direction("Right"),
}


def main():
    origin_cell = make_labyinth()
    player = Player(origin_cell)
    winning_cell = False
    print("Begin!")
    while not winning_cell:
        movement = getch.getch().upper()
        movements[movement](player)
        winning_cell = player.current_cell.is_winning_cell

    print("Congrats! You win!")


if __name__ == "__main__":
    main()
