import petname, random, json, uuid, time
from datetime import datetime

NUM_ANIMALS = 100 
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
        animal["uid"] = str(uuid.uuid4())
        timestamp = datetime.now()
        animal["created_on"] = timestamp.replace(day=timestamp.day-int(i/10)).strftime("%m/%d/%Y %H:%M:%S")
        animals.append(animal);
        
    data = {
        "animals": animals
    }
    with open("animals.json", "w") as f:
        json.dump(data, f, indent=2)
    
if __name__ == "__main__":
    main()