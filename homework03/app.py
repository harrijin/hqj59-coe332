import flask, json, random

app = flask.Flask(__name__)
with open("animals.json", "r") as f:
    animals = json.load(f)["animals"]

@app.route('/', methods=['GET'])
def homepage():
    print("test")
    helpString = \
        """Welcome to my island!
    Paths:
        /animal - Returns a random animal
        /animals - Returns a list of all animals
        /animals/count - Returns total number of animals
        /animals/head/<head> - Returns a list of all animals with specified head
        /animals/arms/<arms> - Returns a list of all animals with specified arms
        /animals/legs/<legs> - Returns a list of all animals with specified legs
        /animals/tails/<tails> - Returns a list of all animals with specified tails
     
    Optional Parameters:
        num - Use to specify number of animals to return for a given noun"""
    return helpString


@app.route('/animals', methods=['GET'])
def get_data():
    return flask.jsonify(animals)

@app.route('/animals/head/<head>', methods=['GET'])
def get_animal_head(head):
    num = flask.request.args.get('num')
    output = [animal for animal in animals if animal["head"] == head]
    if num:
        try:
            maxIndex = min(int(num), len(output))
            output = output[0:maxIndex]
        except:
            print("ERROR: num must be of type int")
    return flask.jsonify(output)

@app.route('/animals/arms/<arms>', methods=['GET'])
def get_animal_arms(arms):
    num = flask.request.args.get('num')
    output = [animal for animal in animals if animal["arms"] == int(arms)]
    if num:
        try:
            maxIndex = min(int(num), len(output))
            output = output[0:maxIndex]
        except:
            print("ERROR: num must be of type int")
    return flask.jsonify(output)

@app.route('/animals/legs/<legs>', methods=['GET'])
def get_animal_legs(legs):
    print(type(legs))
    num = flask.request.args.get('num')
    output = [animal for animal in animals if animal["legs"] == int(legs)]
    if num:
        try:
            maxIndex = min(int(num), len(output))
            output = output[0:maxIndex]
        except:
            print("ERROR: num must be of type int")
    return flask.jsonify(output)

@app.route('/animals/tails/<tails>', methods=['GET'])
def get_animal_tails(tails):
    num = flask.request.args.get('num')
    output = [animal for animal in animals if animal["tail"] == int(tails)]
    if num:
        try:
            maxIndex = min(int(num), len(output))
            output = output[0:maxIndex]
        except:
            print("ERROR: num must be of type int")
    return flask.jsonify(output)
    
@app.route('/animal', methods=['GET'])
def get_animal():
    num = flask.request.args.get('num')
    if not num:
        return flask.jsonify(random.choice(animals))
    output = list()
    for i in range(int(num)):
        animal = None
        while(not animal):
            animal = random.choice(animals)
            # prevent duplicates
            if animal in output:
                animal = None
            else:
                output.append(animal)
    return flask.jsonify(output)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
