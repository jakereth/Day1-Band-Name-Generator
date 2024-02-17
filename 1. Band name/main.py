#import random for random number generating
import random

#
print("Welcome to the band name generator!")

#get inputs for each variable
a1 = input("Which city did you grow up in? ")
a2 = input("What was the name of one of your pets? ")
a3 = input("What is your favorite animal? ")
a4 = input("What is the first object to your right? ")
a5 = input("List the name of a chess piece! ")
a6 = input("Pick a random color! ")
a7 = input("Name a car part! ")
a8 = input("Name a season of the year! ")
a9 = input("Name a type of vehicle! ")

#set words variable equal to list of inputs
words = [a1, a2, a3, a4, a5, a6, a7, a8, a9]


#loop 10 times randomly shuffling the inputs
for i in range(10):
    random.shuffle(words)
    band_name = ' '.join(words[:2])
    print("Your band name could be:", band_name)