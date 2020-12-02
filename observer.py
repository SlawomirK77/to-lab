from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """Subscribe method"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """Unsubscribe method"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """Notify method"""


class Subscription(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, string):
        for observer in self._observers:
            observer.notify(self, string)


class ISubscriber(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """Subscribe method"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """Unsubscribe method"""

    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        """Receive notifications"""


class Subscriber(ISubscriber):
    def __init__(self, observable, filename):
        #observable.subscribe(self)
        self.filename = filename

    def subscribe(self, observable):
        observable.subscribe(self)

    def unsubscribe(self, observable):
        observable.unsubscribe(self)

    def notify(self, observable, string):
        with open(self.filename, "a") as f:
            f.write(string + "\n")
        #print("Subscriber received", string)

if __name__ == "__main__":
    sub = Subscription()

    user1 = Subscriber(sub, "data1.txt")
    user2 = Subscriber(sub, "data2.txt")
    sub.notify("No sub")

    user1.subscribe(sub)
    user2.subscribe(sub)
    sub.notify("first message")

    user1.unsubscribe(sub)
    sub.notify("second message")

    user1.subscribe(sub)
    sub.notify("third message")
