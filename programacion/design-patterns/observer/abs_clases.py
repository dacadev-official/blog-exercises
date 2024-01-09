from abc import ABC, abstractmethod

class Suscriber(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, value) -> None:
        raise NotImplementedError("You must implement this method")


class Publisher(ABC):
    def __init__(self):
        self.subscribers: list[Suscriber] = list()

    def add_suscriber(self, subscriber: Suscriber):
        self.subscribers.append(subscriber)

    def remove_suscriber(self, suscriber: Suscriber):
        self.subscribers.remove(suscriber)

    def notify_suscribers(self, value):
        for suscriber in self.subscribers:
            suscriber.update(value)

class PublisherImprove(ABC):
    def __init__(self) -> None:
        self.subscribers: list[Suscriber] = list()
        self._value = None
    
    def add_suscriber(self, subscriber: Suscriber):
        self.subscribers.append(subscriber)

    def remove_suscriber(self, suscriber: Suscriber):
        self.subscribers.remove(suscriber)

    def notify_suscribers(self):
        for suscriber in self.subscribers:
            suscriber.update(self._value)
    
    @property
    def get_value(self):
        return self._value