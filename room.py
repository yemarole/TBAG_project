class Room:
    def __init__(self, room_name):
        self._name = room_name
        self._description = None
        self.linked_rooms = {}
        self._character = None
        self.items = []
        self.locked = False

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, room_description):
        self._description = room_description

    def describe(self):
        print(self._description)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, room_name):
        self._name = room_name

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, new_character):
        self._character = new_character

    def link_room(self, room_to_link, direction, locked=False):
        self.linked_rooms[direction] = room_to_link
        if locked:
            room_to_link.locked = True

    def get_details(self):
        print(f"You are now in the {self._name}")
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}.")
        if self.character is not None:
            print(f"{self._character.name} is in this room!")
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def unlock(self):
        self.locked = False
        print(f"The door to the {self.name} is now unlocked.")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self
