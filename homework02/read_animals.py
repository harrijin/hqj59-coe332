#!/usr/bin/env python3
import json, random, sys

def generate_id(animal: dict):
    """Generate a unique id of the form 'hbb##aall' for a given animal
        -'h': the third letter of the head
        -'bb##': the first letter of each of the two animals followed by the total length of the body (with a leading zero if necessary)
        -'a': number of arms divided by 2
        -'l': number of legs divided by 3
    """
    assert isinstance(animal, dict), "Input to this function should be a dict"
    keys = animal.keys
    h = animal["head"][2]
    body = animal["body"]
    bb = body[0] + body[body.index('-')+1] + f"{len(body):02d}"
    a = str(int(animal["arms"]/2))
    l = str(int(animal["legs"]/3))
    id = f"{h+bb+a+l}"
    return id

def main():
    with open(sys.argv[1], "r") as f:
        animals = json.load(f)
        
    print(random.choice(animals["animals"]))
    ids = set()
    for animal in animals["animals"]:
        ids.add(generate_id(animal))
    print(ids)

if __name__ == '__main__':
    main()
