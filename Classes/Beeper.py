class Beeper:

    def __init__(self):
        self._observers = []

    def subscribe(self, subscriber):
        self._observers.append(subscriber)

    def count(self, count):
        if(count % 2 == 0):
            self._beep()

    def _beep(self):
        print("I'm beeping")
        for x in self._observers:
            x.receive_beep()
