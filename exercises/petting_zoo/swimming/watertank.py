class WaterTank:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "super amazing water animals"
        self.animals = list()

    def __str__(self):
        return f"You can find these {self.description} in {self.attraction_name}"

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]
