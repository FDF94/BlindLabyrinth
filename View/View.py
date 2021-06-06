class View:

    def receive_beep(self):
        print("Beep!")

    def wall_contact(self, event):
        events = {
            "walk_into": lambda: print("Ouch, there's a wall"),
            "knock": lambda: print("Knock knock")
        }
        events[event]()

    def cell_event(self, event):
        events = {
            "whoosh": lambda: print("Whoosh!"),
            "puddle": lambda: print("Splash!")
        }
        events[event]()

    def player_event(self, event, args):
        events = {
            "no_beep": lambda x: print("No beeper left :("),
            "turn": lambda direction: print(f"Now facing {direction}")
        }
        events[event](args)
