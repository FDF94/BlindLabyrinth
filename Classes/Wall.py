class Wall:

    def __init__(self):
        self._observers = []

    def subscribe(self, subscriber):
        self._observers.append(subscriber)

    def walk_into(self) -> None:
        for x in self._observers:
            x.wall_contact("walk_into")

    def knock(self) -> None:
        for x in self._observers:
            x.wall_contact("knock")
