from datetime import date
from animal import Animal

class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True


        # self.name = name
        # self.species = species
        # self.date_added = date.today()
        # # self.food = food
        # self.__chip_num = chip_num

    # def feed(self):
    #     print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    # def __str__(self):
    #     return f"{self.name} is a {self.species}"

    # @property
    # def chip_num(self):
    #     return self.__chip_num

    # @chip_num.setter
    # def chip_num(self, number):
    #     pass