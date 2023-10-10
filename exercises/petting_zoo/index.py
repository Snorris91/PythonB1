# import the python datetime module to help us create a timestamp

from animal import Catfish, Shark, Whale, Seal, Dolphin, Llama, Dog, Goat, Rabbit, Elephant, Toad, Frog, Gator, Turtle, Snake
from attractions import WaterTank, PettingZoo, SlitherPit



miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Afternoon", "Kibbits", 51)
leo = Dog("Leo", "Poodle", "Morning", "The Big Chow", 11)
tiger = Goat("Tiger", "Mini Goat", "Afternoon", "Mouse", 21)
thumper = Rabbit("Thumper", "Jack-Rabbit", "Morning", "Kibbits", 31)
dumbo = Elephant("Dumbo", "Big Elephant", "Evening", "Peanuts", 41)

steve = Frog("Steve", "Jumping Frog", "Flies", 12)
derek = Toad("Derek", "Brown Toad", "Bugs", 22)
dav = Snake("Dav", "Diamond Back Snake", "Mice", 32)
greg = Gator("Greg", "Alligator", "Chicken", 42)
val = Turtle("Val", "Snapping Turtle", "Kelp", 52)

george = Dolphin("George", "Bottle-Nose Dolphin", "Kelp", 13)
fred = Catfish("Fred", "Catfish", "Chicken", 23)
ron = Shark("Ron", "Great White Shark", "Chicken", 33)
ginny = Whale("Ginny", "Killer Whale", "Plankton", 43)
molly = Seal("Molly", "Lion", "Fish", 53)
bob = Seal("Bob", "Canada Goose", "Watercress Sandwiches", 63)

fluffy_town = PettingZoo("Fluffy Town", "Warm and Cuddly critters")
fluffy_town.add_animal_pythonic(leo)
fluffy_town.add_animal_pythonic(miss_fuzz)
fluffy_town.add_animal_pythonic(tiger)
fluffy_town.add_animal_pythonic(thumper)
fluffy_town.add_animal_pythonic(dumbo)
fluffy_town.add_animal_pythonic(ron)


deep_sea = WaterTank("Aquarius", "Awesome Water Creatures")
deep_sea.add_animal(george)
deep_sea.add_animal(fred)
deep_sea.add_animal(ron)
deep_sea.add_animal(ginny)
deep_sea.add_animal(molly)
deep_sea.add_animal(bob)

wetlands = SlitherPit("Jumanji", "The Vile Fiends")
wetlands.add_animal(steve)
wetlands.add_animal(greg)
wetlands.add_animal(val)
wetlands.add_animal(derek)
wetlands.add_animal(dav)


print(f"{leo.name} is a {leo.species}! They were added on {leo.date_added}.")
steve.feed()

print(fluffy_town)
for animal in fluffy_town.animals:
    print(f"* {animal.name} the {animal.species}")

print(deep_sea)
for animal in deep_sea.animals:
    print(f"* {animal.name} the {animal.species}")

print(wetlands)
for animal in wetlands.animals:
    print(f"* {animal.name} the {animal.species}")

leo.chip_num = 54654
print(leo.chip_number)
leo.feed()
leo.run()
leo.swim()


# print(deep_sea.last_critter_added)


# attributes=vars(miss_fuzz)
# for key in attributes.keys():
#     print(f"{key}: {attributes[key]}")
