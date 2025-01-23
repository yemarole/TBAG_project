class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self.inventory = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, item_name):
        self._name = item_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, item_description):
        self._description = item_description

    def __str__(self):
        return f"{self._name}: {self._description}"

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"{self.name} is not currently holding {item.name}")

    def list_items(self):
        if self.inventory:
            print(f"{self.name} has the following items:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print(f"{self.name}'s inventory is empty.")
