import flask, json, random, redis, datetime

app = flask.Flask(__name__)
rd = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/', methods=['GET'])
def homepage():
    helpString = \
        """
Welcome to Dr. Moreau's island!

Routes:
    /loadAnimals - Load default animals (found in animals.json)
    /numAnimals - Returns total number of animals
    /animal/<uid> - Returns animal with corresponding uid
    /animal/<uid>?<attribute>=<newValue> - Edits animal with corresponding uid by the given attribute/value. Returns edited animal
    /animals - Returns all animals
    /animals?start=YYYYMMDD&end=YYYYMMDD - Returns animals created between given dates, inclusive (only one argument is required)
    /delete - Deletes all animals ( murderer!!! >:( ). Returns number of animals deleted
    /delete?start=YYYYMMDD&end=YYYYMMDD - Deletes animals created between given dates, inclusive (only one argument is required). Returns number of animals deleted
    /averageLegs - Returns average number of legs per animal
    
        """
     
    return helpString

@app.route('/loadAnimals', methods=['GET'])
def loadAnimals():
    with open("animals.json", "r") as f:
        animals = json.load(f)
    for animal in animals["animals"]:
        rd.hmset(animal["uid"], animal)
    return "Loaded animals.json \n"

@app.route('/numAnimals', methods=['GET'])
def numAnimals():
    return str(rd.dbsize()) + " animals in database\n"

@app.route('/animal/<uid>', methods=['GET'])
def getAnimal(uid):
    if not rd.exists(uid):
        return "ERROR: No animal found with uid " + uid + "\n"
    arguments = flask.request.args
    for key, value in arguments.items():
        rd.hset(uid, key, value)
    animal = {key.decode('utf-8'): value.decode('utf-8') for key, value in rd.hgetall(uid).items()}
    return flask.jsonify(animal)
    
@app.route('/animals', methods=['GET'])
def getAnimals():
    start = flask.request.args.get("start")
    end = flask.request.args.get("end")
    minDate = None
    maxDate = None
    if start:
        year = int(start[0:4])
        month = int(start[4:6])
        day = int(start[6:8])
        minDate = datetime.date(year, month, day)
    if end:
        year = int(end[0:4])
        month = int(end[4:6])
        day = int(end[6:8])
        maxDate = datetime.date(year, month, day)
    output = list()
    for uid in rd.keys():
        animal = {key.decode('utf-8'): value.decode('utf-8') for key, value in rd.hgetall(uid).items()}
        # Check if date limits have been set
        if minDate or maxDate:
            createdOn = animal["created_on"]
            month = int(createdOn[0:2])
            day = int(createdOn[3:5])
            year = int(createdOn[6:10])
            creationDate = datetime.date(year, month, day)
            # Check if creation date is within range
            if (minDate and creationDate < minDate) or (maxDate and creationDate > maxDate):
                continue
        output.append(animal)
    return flask.jsonify(output)

@app.route('/delete', methods=['GET'])
def deleteAnimals():
    numDeleted = 0
    start = flask.request.args.get("start")
    end = flask.request.args.get("end")
    minDate = None
    maxDate = None
    if start:
        year = int(start[0:4])
        month = int(start[4:6])
        day = int(start[6:8])
        minDate = datetime.date(year, month, day)
    if end:
        year = int(end[0:4])
        month = int(end[4:6])
        day = int(end[6:8])
        maxDate = datetime.date(year, month, day)
    toDelete = list()
    for uid in rd.keys():
        animal = {key.decode('utf-8'): value.decode('utf-8') for key, value in rd.hgetall(uid).items()}
        # Check if date limits have been set
        if minDate or maxDate:
            createdOn = animal["created_on"]
            month = int(createdOn[0:2])
            day = int(createdOn[3:5])
            year = int(createdOn[6:10])
            creationDate = datetime.date(year, month, day)
            # Check if creation date is within range
            if (minDate and creationDate < minDate) or (maxDate and creationDate > maxDate):
                continue
        rd.delete(uid)
        numDeleted = numDeleted + 1
    return str(numDeleted) + " animals deleted"

@app.route('/averageLegs', methods=['GET'])
def averageLegs():
    totalLegs = 0
    for uid in rd.keys():
        totalLegs = totalLegs + int(rd.hget(uid, "legs"))
    return "Average number of legs per animal: " + str(totalLegs/rd.dbsize()) + "\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
