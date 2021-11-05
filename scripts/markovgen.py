import sys
from npcgen import SPECIAL, SKILLS


def generic_gen(elements: list):
    probabilities = []
    for node in elements:
        print(f"\n==={node}=== Input -- to end")
        weights = []
        for weight in elements:
            p = input(f"Current: {weight} >> ")
            if p == '--':
                to_split = 1.0 - sum(weights)
                remaining_stats = elements[elements.index(weight):]
                for _ in remaining_stats:
                    weights.append(to_split / len(remaining_stats))
                break
            weights.append(float(p))
            print(weights)
        if sum(weights) > 1.0:
            raise ValueError("Weights are over 1")
        miss = 1.0 - sum(weights)
        print(f"{sum(weights)} -> {miss}")
        if miss > 0.0:
            # increments the heaviest node with the marginal missing value
            weights[weights.index(max(weights))] += miss
            print(sum(weights))
        print(weights)
        probabilities.append(weights)
    return probabilities

def gen_skills():
    '''Generates markov probabilities for all Skills of FNV'''
    return generic_gen(elements=SKILLS)

def gen_special():
    '''Generates markov probabilities for all SPECIAL of FNV'''
    return generic_gen(elements=SPECIAL)


def gen(type:str):
    ret = None
    if type == 'skills':
        return gen_skills()
    elif type == 'special':
        return gen_special()
    return ret
    print("Done")

if __name__ == "__main__":
    chain = sys.argv[1].lower()
    if chain in ['skills', 'special']:
        print(gen(type=chain))
    else:
        print("Use either 'skill' or 'special' as parameter, please\n\tpipenv run python markovgen.py [skills|specials]")

