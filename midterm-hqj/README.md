# Midterm Project

This directory contains my submission for the midterm project. Build and run my Flask app and Redis in separate Docker containers using the command below:

```
docker-compose up -d --build
```

Query the API using the following command:

```
curl 'localhost:5013/<route>'
```

where route is the API route (see below). Use `generate_animals.py` to generate 100 animals, 10 for each of the past 10 days. 

## API routes and parameters

```
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
```