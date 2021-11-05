import re
import sys
import random

from npcgen.classes import Ranger


def build_new_npc(class_name):
    classes = {"ranger": Ranger}
    level = random.randint(1, 10)
    return classes.get(class_name)(level=level)


def generate_npcs():
    generated_npcs = []
    for arg in sys.argv[1:]:
        # split the parameter
        amt, npc_type = re.match(r"([0-9]*)([a-z]*)", arg.lower()).groups()
        # generate the indicated number of NPCs
        for i in range(int(amt)):
            new_npc = build_new_npc(npc_type)
            generated_npcs.append(new_npc)
        for npc in generated_npcs:
            print(npc)
