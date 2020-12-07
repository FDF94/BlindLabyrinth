from Classes.Player import Player
import getch

movements = {
    "E":lambda x: x.turn_right(),
    "Q":lambda x: x.turn_left()
}

def main():
    player = Player()
    while True:
        movement = getch.getch().upper()
        movements[movement](player)
        print("Now facing:", player._facing)

if __name__ == "__main__":
    main()