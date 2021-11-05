from pydtmc import MarkovChain

from npcgen import SPECIAL

p = ((0.7, 0.3), (0.5, 0.2))
mc = MarkovChain(p, SPECIAL)

print(mc.walk(5))
