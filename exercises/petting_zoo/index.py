# import the python datetime module to help us create a timestamp
from datetime import date
from swimming import Catfish, Shark, Whale, Seal, Dolphin
from walking import Llama, Dog, Goat, Rabbit, Elephant
from slithering import Toad, Frog, Gator, Turtle, Snake


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Afternoon", "Kibbits")
leo = Dog("Leo", "Poodle", "Morning", "The Big Chow")
tiger = Goat("Tiger", "Mini Goat", "Afternoon", "Mouse")
thumper = Rabbit("Thumper", "Jack-Rabbit", "Morning", "Kibbits")
dumbo = Elephant("Dumbo", "Big Ears", "Evening", "Peanuts")

steve = Frog("Steve", "Jumping Frog", "Pond", "Flies")
derek = Toad("Derek", "Brown Toad", "Pond", "Bugs")
dav = Snake("Dav", "Diamond Back", "Pond", "Mice")
greg = Gator("Greg", "Alli", "Pond", "Chicken")
val = Turtle("Val", "Turtle", "Pond", "Kelp")

george = Dolphin("George", "Bottle-Nose", "Tank", "Kelp")
fred = Catfish("Fred", "Catfish", "Tank", "Chicken")
ron = Shark("Ron", "Great White", "Tank", "Chicken")
ginny = Whale("Ginny", "Killer", "Tank", "Plankton")
molly = Seal("Molly", "Lion", "Tank", "Fish")

print(f"{leo.name} is a {leo.species}! They were added on {leo.date_added}.")
leo.feed()
print(leo)
