class Observable(object):
    """ Observable class"""

    def __init__(self):
        self.__observers = []

    def register(self, *observer):
        for item in observer:
            if item in self.__observers:
                continue
            self.__observers.append(item)

    def unregister(self, observer):
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self)
