from datetime import date

class Gator:
    def __init__(self, name, species, location, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.food = food
        self.__chip_num = chip_num
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @property
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter
    def chip_num(self, number):
        pass