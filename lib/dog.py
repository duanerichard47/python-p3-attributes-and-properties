#!/usr/bin/env python3

class Dog:

    def get_name(self):
        print("Retrieving the name of the dog")
        return self._name
    
    
    def set_name(self, name):
        #if ((name != "" or type(name) == (str)) and (0 <= len(name) <= 25)):
        if (type(name) == str) and (0 < len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    
    def set_breed(self,breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
   
        if breed in approved_breeds:
            self._breed = breed
        else:
            print(f"Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)


    

            
