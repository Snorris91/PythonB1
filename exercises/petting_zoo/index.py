# import the python datetime module to help us create a timestamp
from datetime import date
from animal import Animal
from swimming import Catfish, Shark, Whale, Seal, Dolphin, WaterTank
from walking import Llama, Dog, Goat, Rabbit, Elephant, PettingZoo
from slithering import Toad, Frog, Gator, Turtle, Snake, SlitherPit


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Afternoon", "Kibbits", 5)
leo = Dog("Leo", "Poodle", "Morning", "The Big Chow", 1)
tiger = Goat("Tiger", "Mini Goat", "Afternoon", "Mouse", 2)
thumper = Rabbit("Thumper", "Jack-Rabbit", "Morning", "Kibbits", 3)
dumbo = Elephant("Dumbo", "Big Elephant", "Evening", "Peanuts", 4)

steve = Frog("Steve", "Jumping Frog", "Pond", "Flies", 1)
derek = Toad("Derek", "Brown Toad", "Pond", "Bugs", 2)
dav = Snake("Dav", "Diamond Back Snake", "Pond", "Mice", 3)
greg = Gator("Greg", "Alligator", "Pond", "Chicken", 4)
val = Turtle("Val", "Snapping Turtle", "Pond", "Kelp", 5)

george = Dolphin("George", "Bottle-Nose Dolphin", "Tank", "Kelp", 1)
fred = Catfish("Fred", "Catfish", "Tank", "Chicken", 2)
ron = Shark("Ron", "Great White Shark", "Tank", "Chicken", 3)
ginny = Whale("Ginny", "Killer Whale", "Tank", "Plankton", 4)
molly = Seal("Molly", "Lion", "Tank", "Fish", 5)

fluffy_town = PettingZoo("Fluffy Town")
fluffy_town.add_animal(leo)
fluffy_town.add_animal(miss_fuzz)
fluffy_town.add_animal(tiger)
fluffy_town.add_animal(thumper)
fluffy_town.add_animal(dumbo)

deep_sea = WaterTank("Aquarius")
deep_sea.add_animal(george)
deep_sea.add_animal(fred)
deep_sea.add_animal(ron)
deep_sea.add_animal(ginny)
deep_sea.add_animal(molly)

wetlands = SlitherPit("Jumanji")
wetlands.add_animal(steve)
wetlands.add_animal(greg)
wetlands.add_animal(val)
wetlands.add_animal(derek)
wetlands.add_animal(dav)

print(fluffy_town)
print(f"{leo.name} is a {leo.species}! They were added on {leo.date_added}.")
leo.feed()
print(leo)

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
print(leo.chip_num)
print(fluffy_town.last_critter_added)


attributes=vars(miss_fuzz)
for key in attributes.keys():
    print(f"{key}: {attributes[key]}")
