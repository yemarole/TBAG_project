class Character:

    def __init__(self, char_name, char_description):
        self.name = char_name.capitalize()
        self.description = char_description
        self.conversation = None
        self.inventory = []

    def describe(self):
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"{self.name} does not have {item}.")

    def list_items(self):
        if self.inventory:
            print(f"{self.name} has the following items:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print(f"{self.name}'s inventory is empty")


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.bribed = False
        self.asleep = False

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You have defeated {self.name} with the {combat_item}!")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    def steal(self):
        pass

    def bribe(self, item):
        if not self.bribed:
            self.bribed = True
            self.add_item(item)
            print(f"You have bribed {self.name} with {item.name}")
        else:
            print(f"{self.name} laughs at you and rejects your bribe.")

    def send_to_sleep(self):
        if not self.asleep:
            self.asleep = True
            print(f"You have sent {self.name} to sleep.")
        else:
            print(f"{self.name} is already asleep.")


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.friendship_level = 0

    def hug(self):
        self.friendship_level += 1
        print(
            f"You just hugged {self.name}. Friendship level is now {self.friendship_level}."
        )

    def gift(self, gift):
        self.friendship_level = +2
        self.add_item(gift)
        print(
            f"You gifted {self.name} a {gift.name}. Friendship level is now {self.friendship_level}"
        )
