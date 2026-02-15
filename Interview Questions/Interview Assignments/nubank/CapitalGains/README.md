## Core Features

- For set of simulations provided, Calculates tax per operation within the simulation

## Installation

### Dependencies:

- install python version >=3.9
- For running test install pytest version >= 9
- install python package manager pip >= 21

### Running the application:

**Locally:**

Depending on how your environment variable for installation of python is configured - `python3 vs python`

```
python3 main.py
```

**Running with file data:**

Add your data in repose folder.

```
python3 main.py < ./repos/data.txt
```

**Docker**

Building the docker image:

`docker build -t capital-gains .`

Initializing the container

`docker run -it capital-gains`

File example
`docker run -i capital-gains < repos/data.txt`

## Running tests:

Run both integration and unit test

`pytest`

Run unit test:

`pytest unit`

Run integration test:

`pytest integration`
