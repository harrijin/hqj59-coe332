#!/usr/bin/env python3
import petname, random, json, sys

NUM_ANIMALS = 20
HEADS = ["snake", "bull", "lion", "raven", "bunny"]

def main():
    animals = []
    for i in range(NUM_ANIMALS):
        animal = dict()
        animal["head"] = random.choice(HEADS)
        animal["body"] = petname.name() + "-" + petname.name()
        animal["arms"] = random.randint(1,5)*2
        animal["legs"] = random.randint(1,4)*3
        animal["tail"] = animal["arms"] + animal["legs"]
        animals.append(animal)
    data = {
        "animals": animals
    }
    with open(sys.argv[1], "w") as out:
        json.dump(data, out, indent=2)
    
if __name__ == "__main__":
    main()
