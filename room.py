class Room:
    def __init__(self, room_name):
        self._name = room_name
        self._description = None
        self.linked_rooms = {}
        self._character = None

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

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self._name)
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}.")
        if self.character is not None:
            print(f"{self._character.name} is here!")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self
