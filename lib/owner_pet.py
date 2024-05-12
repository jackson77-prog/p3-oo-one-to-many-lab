class Owner:
   def __init__(self, name):
       self.name = name
       self._pets = []


   def pets(self):
       return self._pets


   def add_pet(self, pet):
       if not isinstance(pet, Pet):
           raise Exception("Pet must be an instance of the Pet class")
       pet.owner = self
       self._pets.append(pet)


   def get_sorted_pets(self):
       return sorted(self._pets, key=lambda pet: pet.name)




class Pet:
   PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
   all = []


   def __init__(self, name, pet_type, owner=None):
       if pet_type not in self.PET_TYPES:
           raise Exception("Invalid pet type")
       self.name = name
       self.pet_type = pet_type
       self.owner = owner
       if owner:
           owner.add_pet(self)
       self.all.append(self)  # Add the current instance to the all list


   @classmethod
   def clear_all(cls):
       """Clear the all list"""
       cls.all = []



