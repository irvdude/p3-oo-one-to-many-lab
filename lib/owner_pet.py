from typing import Any


class Pet:
    all = []

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        self.set_pet_type(pet_type)
        Pet.all.append(self)

    def set_pet_type(self, pet_type):
        if pet_type.lower() in self.PET_TYPES:
            self.pet_type = pet_type.lower()
        else:
            raise Exception()

    pass


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception()

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets

    pass
