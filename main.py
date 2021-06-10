from GameState.GameState import GameState
from GameEntities.Player import Player
from GameEntities.Maze import Maze
from GameEntities.Counter import Counter
from GameEntities.Beeper import Beeper
from View.View import View
from HardwareControl.WindowsInput import handle_input

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
}


def main():
    # Initialize all objects
    view = View()
    counter = Counter()
    beeper = Beeper()
    maze = Maze(3, 3, view)
    origin_cell = maze.cells_grid[-1][-1]
    player = Player(origin_cell, beeper)
    winning_cell = False
    game_state = GameState(player, maze)

    # Make subscriptions
    counter.tick_event += beeper.count
    beeper.beep_event += game_state.beep_event
    game_state.sound_event += view.sound_event
    player.turn_event += view.turn_event
    player.no_beeper_event += view.no_beeper_event
    print("\nBegin!")

    while not winning_cell:
        counter.tick()
        movement = handle_input()
        if movement:
            try:
                movements[movement](player)
            except KeyError:
                continue
        winning_cell = player.current_cell.is_winning_cell

    print("Congrats! You win!")


if __name__ == "__main__":
    main()
