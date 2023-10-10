from datetime import date
from .animal import Animal
from movements import Walking, Slithering

class Frog(Animal, Slithering, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        Walking.__init__(self)
