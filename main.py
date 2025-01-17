from room import Room

kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies."
ballroom = Room("ballroom")
ballroom.description = "A vast room with shiny wooden floors."
dining_hall = Room("dining hall")
dining_hall.description = "A large room with ornate golden decorations on each wall."

# print(kitchen.describe())

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# dining_hall.get_details()

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)
