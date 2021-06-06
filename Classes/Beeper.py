class Beeper:

    def __init__(self):
        self._observers = []
        self.is_set = False
        self.beeps_allowed = False

    def subscribe(self, subscriber):
        self._observers.append(subscriber)

    def count(self, count):
        if(count % 5 == 0 and self.is_set and self.beeps_allowed):
            self._beep()

    def _beep(self):
        for x in self._observers:
            x.receive_beep()
