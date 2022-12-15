obj_test = {
    "obj": ["interactions", "health", "damage"]
}

obj = {
    "chair_1": [["Interact with chair", "Sit on chair", "Attack chair"], 10],
    "sword_1": [["Interact with sword", "Take sword", "Attack sword"], 1000, 2],
    "person_1": ["interact with person", 120] #temp: make char sheets with stats, potentially randomised
}

location_test = {
    "location": ["description", "options"]
}

location = {
    "house_1": ["You are inside a house with a pretty interior", ["Leave house"]],
    "outside house": ["There is a pretty house contrasted to the forboding forest, "
    "you spot an intimidating person leaning against the house", ["Enter house", "Enter forest"]],
    'forest': ['nothing', 'nothing']
}

locations = {
    'house_1': [['outside house'], [['sword_1', False], ['chair_1', True]], ["You are inside a house with a pretty interior", ["Leave house"]]],
    'outside house': [['house_1', 'forest'], [['person_1', True]], ["There is a pretty house contrasted to the forboding forest, "
    "you spot an intimidating person leaning against the house", ["Enter house", "Enter forest"]]],
    'forest': [['outside house'], [None]]
}
print(len(locations['house_1'][1]))

stats = {
    "end": 5, #endurance
    "vit": 10, #vitality
    "dex": 10, #dexterity
    "agl": 10, #agility
    "per": 10, #perception
    "cha": 10, #charisma
    "int": 10, #intelligence
    "wis": 10, #wisdom
    "str": 10, #strength
    "age": 20 #age
}