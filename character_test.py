from character import Character, Enemy

# player_inventory = ["sword", "armor", "shield"]
dave = Enemy("Dave", "Dave is a smelly zombie")
dave.describe()

dave.set_conversation("Brainnssssss!")
dave.talk()

dave.set_weakness("cheese")
fight_with = input(f"What will you fight with?: ")

dave.fight(fight_with)
