class Item:
    def __init__(self):
        self._name = None
        self._description = None

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
