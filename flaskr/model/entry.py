
class Entry():
    def __init__(self, id, title, text):
        self.id, self.title, self.text = id, title, text

    def storage(self):
        return dict(self.__dict__)
