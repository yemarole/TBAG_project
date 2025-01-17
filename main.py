from room import Room

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining hall")

kitchen.set_description("A dank and dirty room buzzing with flies.")

print(kitchen.describe())
