from Classes.Event import Event


class Beeper:

    def __init__(self):
        self.beep_event = Event()
        self.is_set = False
        self.beeps_allowed = False

    def count(self, count):
        if(count % 5 == 0 and self.is_set and self.beeps_allowed):
            self.beep_event.notify()