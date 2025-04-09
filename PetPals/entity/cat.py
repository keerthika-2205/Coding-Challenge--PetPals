from entity.pet import Pet

class Cat(Pet):
    def __init__(self, name=None, age=None, breed=None, cat_color=None):
        super().__init__(name, age, breed)
        self._cat_color = cat_color

    @property
    def cat_color(self):
        return self._cat_color

    @cat_color.setter
    def cat_color(self, value):
        self._cat_color = value

    def __str__(self):
        return f"Cat(Name: {self._name}, Age: {self._age}, Breed: {self._breed}, CatColor: {self._cat_color})"