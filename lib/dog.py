#!/usr/bin/env python3

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
    def get_name(self):
        print("Retrieving the name of the dog")
        return self.name
    
    
    def set_name(self,name):
        if (type(name) == (str)) and (0 <= len(name) <= 25):
            print(f"Setting the name of the dog to {name}.")
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        print("Retrieving the breed of the dog")
        return self.breed
    
    
    def set_name(self,breed):
        if breed in approved_breeds == true:
            print(f"Setting the name of the dog to {breed}.")
            self.breed = breed
        else:
            print(f"The breed must be in the following list of dog breeds:{approved_breeds}")
