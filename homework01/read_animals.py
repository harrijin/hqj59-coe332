import json, random

def main():
    with open("animals.json", "r") as f:
        animals = json.load(f)
        
    animal = random.choice(animals["animals"])
    print(animal)

if __name__ == '__main__':
    main()