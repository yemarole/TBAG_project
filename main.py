from room import Room

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with shiny wooden floors.")
dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# print(kitchen.describe())

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dining_hall.get_details()
