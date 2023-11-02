from .attractions import Attraction


class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.shift:
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError:
            print(
                f"{animal.name} does not like to be petted, so please do not put it in the {self.attraction_name} attraction!")
