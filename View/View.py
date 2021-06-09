from Infrastructure.Sound import Sound


class View:

    def sound_event(self, sound: Sound):
        print(f"You hear {sound.sound}, coming " +
              f"from the {sound.direction}")
        if sound.is_muffled:
            print("It comes from behind a wall")

    # Wall events
    def knock_event(self):
        print("Knock knock")

    def walk_into_event(self):
        print("Ouch, there's a wall")

    # Cell events
    def whoosh_event(self):
        print("Whoosh!")

    def puddle_event(self):
        print("Splash!")

    # Player events
    def no_beeper_event(self):
        print("No beeper left :(")

    def turn_event(self, direction):
        print(f"Now facing {direction}")
