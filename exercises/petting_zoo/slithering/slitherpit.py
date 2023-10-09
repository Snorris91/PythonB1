class SlitherPit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cold-blooded fiends"
        self.animals = list()
    def __str__(self):
        return f"You can find these {self.description} in {self.attraction_name}"
    def add_animal(self, animal):
        self.animals.append(animal)
