from room import Room
from character import Enemy

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

dave = Enemy("Dave", "Dave is a smelly zombie")
dave.set_conversation("Brrlgrh... must eat... rgrhl... braaaiinnnsss...")
dave.set_weakness("cheese")

dining_hall.character = dave

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.character
    if inhabitant is not None:
        inhabitant.describe()
        print(
            f"[If you want to talk then type 'talk' & if you want to fight type 'fight']"
        )

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "fight":
        print("What is your weapon of choice?: ")
        combat_item = input("> ")
        if not inhabitant.fight(combat_item):
            print("Game Over!")
            break
