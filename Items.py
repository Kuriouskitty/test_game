items = [
    ["sword", "temporary", 100, 1, "unequipped"],
    ["key", "temporary", 5, 0, None]
]
inventory = [[None] * 5] * 100
inventory[0] = items[1]
inventory[1] = items[0]
print(inventory[0])