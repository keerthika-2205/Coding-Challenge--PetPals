from entity.pet import Pet

class Dog(Pet):
    def __init__(self, name=None, age=None, breed=None, dog_breed=None):
        super().__init__(name, age, breed)
        self._dog_breed = dog_breed

    @property
    def dog_breed(self):
        return self._dog_breed

    @dog_breed.setter
    def dog_breed(self, value):
        self._dog_breed = value

    def __str__(self):
        return f"Dog(Name: {self._name}, Age: {self._age}, Breed: {self._breed}, DogBreed: {self._dog_breed})"