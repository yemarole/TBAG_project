import re
from room import Room
from character import Enemy, Character, Friend
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
kitchen.link_room(dining_hall, "south", locked=True)
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west", locked=True)
ballroom.link_room(dining_hall, "east")

# Create Items
knife = Item("knife", "a sharp kitchen knife")
sword = Item("sword", "an heat imbued magic sword")
shield = Item("shield", "a sturdy shield")
purified_water = Item("purified water", "a bottle of purified water")
key = Item("key", "A gold master key that can unlock any door.")

# Add items to rooms
kitchen.add_item(knife)
dining_hall.add_item(shield)

# Create Dave the Zombie
dave = Enemy("Dave", "Dave is a smelly zombie")
dave.set_conversation("Brrlgrh... must eat... rgrhl... braaaiinnnsss...")
dave.set_weakness("cheese")
dave.add_item(purified_water)

dining_hall.character = dave

# Create a new character in a different room
harry = Enemy("harry", "Harry is a ugly troll")
harry.set_conversation("hehehe, you won't beat me!")
harry.set_weakness("purified water")

ballroom.character = harry

# Create a friend character
aurora = Friend("Aurora", "Aurora is a friendly elf.")
aurora.set_conversation("Hello friend! Nice to see you!")
aurora.add_item(sword)
aurora.add_item(key)


kitchen.character = aurora

# Add a key to the game

# create inventory
inventory = []

# starting room
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.character
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant.list_items()
        print(
            "[Type: 'talk', 'hug', 'gift [item]', 'sleep', 'inventory', 'take [name item]', 'drop [name item]', 'unlock [direction]' or any direction]"
        )

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        if current_room.linked_rooms[command].locked:
            print(
                f"The door to the {current_room.linked_rooms[command].name} is locked."
            )
        else:
            current_room = current_room.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "hug" and isinstance(inhabitant, Friend):
        inhabitant.hug()
    elif command.startswith("gift") and isinstance(inhabitant, Friend):
        item_name = command.split(" ", 1)[1]
        item = next((i for i in inventory if i.name == item_name), None)
        if item:
            inventory.remove(item)
            inhabitant.gift(item)
        else:
            print(f"You don't have {item_name}")
    elif command == "fight":
        print("\n What is your weapon of choice?: ")
        combat_item = input("> ")
        if not inhabitant.fight(combat_item):
            print("Game Over!")
            break
    elif command == "inventory":
        if inventory:
            print("\n You have the following items in your inventory:")
            for item in inventory:
                print(f"- {item.name}: {item.description}")
        else:
            print("Your inventory is empty.")
    elif re.match(r"^pick up \w+", command):
        item_name = command.split(" ", 2)[2]
        item = next((i for i in current_room.items if i.name == item_name), None)
        if item:
            inventory.append(item)
            current_room.remove_item(item)
            print(f"\n You just picked up {item_name} from the {current_room.name}!")
        else:
            print(f"There is no {item_name} here.")
    elif command.startswith("take "):
        item_name = command.split(" ", 1)[1]
        item = next((i for i in inhabitant.inventory if i.name == item_name), None)
        if item:
            inventory.append(item)
            inhabitant.remove_item(item)
            print(f"\n You just took {item_name} from {inhabitant.name}!")
        else:
            print(f"There is no {item_name} here.")
    elif command.startswith("drop "):
        item_name = command.split(" ", 1)[1]
        item = next((i for i in inventory if i.name == item_name), None)
        if item:
            inventory.remove(item)
            current_room.add_item(item)
            print(f"\n You just dropped {item_name} in the {current_room.name}.")
        else:
            print(f"You don't have a {item_name}.")
    elif command.startswith("bribe ") and isinstance(inhabitant, Enemy):
        item_name = command.split(" ", 1)[1]
        item = next((i for i in inventory if i.name == item_name), None)
        if item:
            inventory.remove(item)
            inhabitant.bribe(item)
        else:
            print(f"You don't have a {item_name}.")
    elif command == "sleep" and isinstance(inhabitant, Enemy):
        inhabitant.send_to_sleep()
    elif command.startswith("unlock "):
        direction = command.split(" ", 1)[1]
        if (
            direction in current_room.linked_rooms
            and current_room.linked_rooms[direction].locked
        ):
            key_item = next((i for i in inventory if i.name == "key"), None)
            if key_item:
                current_room.linked_rooms[direction].unlock()
            else:
                print("You don't have a key.")
        else:
            print(f"There is no locked door to the {direction}.")
