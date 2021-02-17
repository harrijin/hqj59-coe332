# Homework #2

This directory contains my submission for homework #2. This is a continuation of homework #1, a .json generator (`generate_animals.py`) and parser (`read_animals.py`).  This assignment adds [ID generation](https://github.com/harrijin/hqj59-coe332/blob/290953f1d2a7139f322eace2a98b4d9cdf09fe96/homework02/read_animals.py#L4) for each animal, a [unit test](https://github.com/harrijin/hqj59-coe332/blob/main/homework02/test_read_animals.py) for the ID generation, and a Docker container for the project.

## Dependencies

To run the scripts directly, [Python 3.6](https://www.python.org) or higher is required. In addition, the [`petname`](https://github.com/dustinkirkland/python-petname) package is required.

```
pip3 install --user petname
```

To build and run the Docker image, [Docker](https://docs.docker.com/engine/install/ubuntu/) is required.

## Installation

Install this project by cloning the repository.

```
git clone https://github.com/harrijin/hqj59-coe332.git
```

Navigate into this directory.

```
cd hqj59-coe332/homework02
```

## Usage

### Running the scripts directly

Generate a list of 20 animals using `generate_animals.py`.

```
python3 generate_animals.py <output file name>
```
Read the list, print a random animal, and generate (and print) ID's using `read_animals.py`. (Use the same file name as above)
```
python3 read_animals.py <input file name>
```

### Running the scripts using a Docker container

Build the docker image using `docker build`

```
docker build -t <name>:<tag> .
```

or pull my docker image from [Docker Hub](https://hub.docker.com/r/harrijin/json-parser)
```
docker pull harrijin/json-parser:1.0
```

The rest of these instructions will assume the image is called `harrijin/json-parser:1.0`.

#### Interactive Docker container

To create an interactive Docker container, run the following:
```
docker run --rm -it -u $(id -u):$(id -g) -v $PWD:/data harrijin/json-parser:1.0 /bin/bash
```
Verify that the shell prompt has changed accordingly. 

Navigate to `/data` and generate animals.
```
cd /data
generate_animals.py <output file name>
```

Read and print a random animal and ID's.
```
read_animals.py <input file name>
```

After exiting the docker container with `exit`, the animal file you generated should be in the current directory. 

#### Non-interactive Docker container

Generate animals:

```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) harrijin/json-parser:1.0 generate_animals.py /data/animals.json
```
Read and print a random animal and ID's.

```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) harrijin/json-parser:1.0 read_animals.py /data/animals.json
```

### Unit testing

This repository includes a unit test for the ID generation function, `test_read_animals.py`. Run the unit test with the following command:

```
python3 test_read_animals.py
```