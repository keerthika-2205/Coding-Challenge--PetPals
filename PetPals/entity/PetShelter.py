from entity.pet import Pet
from entity.iadoptable import IAdoptable

class PetShelter(IAdoptable):
    def __init__(self):
        self._available_pets = []

    def add_pet(self, pet: Pet):
        self._available_pets.append(pet)

    def remove_pet(self, pet: Pet):
        if pet in self._available_pets:
            self._available_pets.remove(pet)
        else:
            raise Exception("Pet not found in shelter")

    def list_available_pets(self):
        return self._available_pets

    def adopt(self):
        return "Pet adopted from shelter"