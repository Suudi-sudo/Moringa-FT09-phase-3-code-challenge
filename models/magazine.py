class Magazine:
    def __init__(self, id, name, category):
        self._id = id  
        self._name = name  
        self._category = category  

# returning the stored id
    @property
    def id(self):
        return self._id  
# returning the stored name

    @property
    def name(self):
        return self._name  
# returning the stored category

    @property
    def category(self):
        return self._category  

    def __repr__(self):
        return f'<Magazine {self.name}>'
