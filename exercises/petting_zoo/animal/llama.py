from datetime import date
from .animal import Animal
from movements import Walking

class Llama(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift
        Walking.__init__(self)
    def feed(self):
        print(f"{self.food} is {self.name}'s favorite food!")
