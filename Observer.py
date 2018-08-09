
class Subject(object):

    def __init__(self):
        self.observers = set()

    def register(self, new_observer):
        self.observers.add(new_observer)

    def unregister(self, observer):
        self.observers.discard(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(observer.name + ',' + message)


class Observer(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def update(message):
        print(message)


# create Subject and observers objects.
newspaper = Subject()
sub1 = Observer('Eduardo')
sub2 = Observer('Carlos')

# add Observers to Subject's list of subscribers.
newspaper.register(sub1)
newspaper.register(sub2)

# notify subscribers for change in state of newspaper.
newspaper.notify('El periódico de hoy te espera')

# delete sub2(Carlos) from subscribers list.
newspaper.unregister(sub2)

# notify updated list of subscribers.
newspaper.notify('El periódico de hoy te espera')