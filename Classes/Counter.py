class Counter:

    def __init__(self):
        self._observers = []
        self._count = 0

    def subscribe(self, subscriber):
        self._observers.append(subscriber)

    def tick(self):
        self._count += 1
        for x in self._observers:
            x.count(self._count)
