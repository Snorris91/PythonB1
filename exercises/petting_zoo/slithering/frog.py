from datetime import date

class Frog:
    def __init__(self, name, species, location, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.food = food
        self.slithering = True
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"