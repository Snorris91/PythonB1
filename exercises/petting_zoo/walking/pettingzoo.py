class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def __str__(self):
        return f"You can find these {self.description} in {self.attraction_name}"
        # {self.animals.name} the {animal.species}"

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]
