SPECIAL = ["S", "P", "E", "C", "I", "A", "L"]
SKILLS = [
    "Barter",
    "Energy Weapons",
    "Explosives",
    "Guns",
    "Lockpick",
    "Medicine",
    "Melee Weapons",
    "Repair",
    "Science",
    "Sneak",
    "Speech",
    "Survival",
    "Unarmed",
]

SKILLS_STAT = {
    "Barter": "C",
    "Energy Weapons": "P",
    "Explosives": "P",
    "Guns": "A",
    "Lockpick": "P",
    "Medicine": "I",
    "Melee Weapons": "S",
    "Repair": "I",
    "Science": "I",
    "Sneak": "A",
    "Speech": "C",
    "Survival": "E",
    "Unarmed": "E",
}

SPECIAL_SKILLS = {
    "S": ["Melee Weapons"],
    "P": ["Energy Weapons", "Explosives", "Lockpick"],
    "E": ["Survival", "Unarmed"],
    "C": ["Barter", "Speech"],
    "I": ["Medicine", "Repair", "Science"],
    "A": ["Guns", "Sneak"],
}

"""
{"S": 0, "P": 0, "E": 0, "C": 0, "I": 0, "A": 0, "L": 0}
{"S": 5, "P": 5, "E": 5, "C": 5, "I": 5, "A": 5, "L": 5}

{
    "Barter": 0,
    "Energy Weapons": 0,
    "Explosives": 0,
    "Guns": 0,
    "Lockpick": 0,
    "Medicine": 0,
    "Melee Weapons": 0,
    "Repair": 0,
    "Science": 0,
    "Sneak": 0,
    "Speech": 0,
    "Survival": 0,
}
"""
