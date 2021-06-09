from Infrastructure.Event import Event


class Counter:

    def __init__(self):
        self.tick_event = Event()
        self._count = 0

    def tick(self):
        self._count += 1
        self.tick_event.notify(self._count)
