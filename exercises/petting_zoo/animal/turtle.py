from datetime import date
from .animal import Animal
from movements import Walking, Slithering

class Turtle(Animal, Walking, Slithering):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        Walking.__init__(self)
        Slithering.__init__(self)



    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    # def __str__(self):
    #     return f"{self.name} is a {self.species}"

    # @property
    # def chip_num(self):
    #     return self.__chip_num

    # @chip_num.setter
    # def chip_num(self, num):
    #     pass
