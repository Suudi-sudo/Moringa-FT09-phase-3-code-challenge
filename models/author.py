class Author:
    def __init__(self, id, name):
        self._id = id  
        self._name = name  
# returning the stored id
    @property
    def id(self):
        return self._id  
# returning the stored name
    @property
    def name(self):
        return self._name  

    def __repr__(self):
        return f'<Author {self.name}>'
