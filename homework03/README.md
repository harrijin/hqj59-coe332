# Homework #3

This directory contains my submission for homework #3. Build and run my Flask app in a Docker container using the commands below:

```
docker build -t <name>:<tag> .
docker run --name "<any name>" -d -p <port#>:5000 <name>
```

For example:
```
docker build -t flask-animals:latest .
docker run --name "flask-animal-demo" -d -p 5013:5000 flask-animals
```

Query the API using the following command:

```
curl localhost:<port>/<path>
```

where port is the port entered in the `docker run` command and path is the API path (see below).

## API Paths and parameters

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