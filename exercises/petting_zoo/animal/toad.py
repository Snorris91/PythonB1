from datetime import date
from .animal import Animal
from movements import Walking, Slithering

class Toad(Animal, Walking, Slithering):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Slithering.__init__(self)
