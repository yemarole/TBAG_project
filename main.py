from room import Room
from character import Enemy, Character
from item import Item

# Set up rooms
kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining hall")

# Set descriptions
kitchen.description = "A dank and dirty room buzzing with flies."
ballroom.description = "A vast room with shiny wooden floors."
dining_hall.description = "A large room with ornate golden decorations on each wall."

# Set room orientation
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Create Dave the Zombie
dave = Enemy("Dave", "Dave is a smelly zombie")
dave.set_conversation("Brrlgrh... must eat... rgrhl... braaaiinnnsss...")
dave.set_weakness("cheese")
inventory = dave.add_item("purified water")

dining_hall.character = dave

# Create a new character in a different room
harry = Enemy("harry", "Harry is a ugly troll")
harry.set_conversation("hehehe, you won't beat me!")
harry.set_weakness("purified water")

ballroom.character = harry

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
    elif command == "inventory":
        inventory.list_items()
    elif command.startswith("take "):
        item_name = command.split(" ", 1)[1]
        item = next((i for i in current_room.items if i.name == item_name), None)
        if item:
            inventory.add_item(item)
            current_room.remove_item(item)
        else:
            print(f"There is no {item_name} here.")
    elif command.startswith("drop "):
        item_name = command.split(" ", 1)[1]
        item = next((i for i in inventory.items if i.name == item_name), None)
        if item:
            inventory.remove_item(item)
            current_room.add_item(item)
        else:
            print(f"You don't have a {item_name}.")
