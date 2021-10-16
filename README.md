# Golden Retriever
Fetches images from the drone!

## Dependencies
- Docker

## Installation and Run
Cd to the repo root where the Dockerfile is and build the image locally:

```
docker image build -t golden .
```
This builds the image called `golden`.

Create and run the container:
```
docker container run --name run-golden golden
```
This creates the docker container named `run-golden` that runs with the default commands set in the Dockerfile's `CMD` instruction.

To customize the commands with the CLI options, can do this instead:
```
docker container run --name run-golden golden python3 app.py --path my_path --url my_url --wait my_wait --ext1 my_ext1 --ext2 my_ext2
```
Set `my_path, my_url, my_wait, my_ext1, my_ext2` as required.

### Testing
Cd to golden-retriever/test and build the test container locally:
```
docker-compose build --parallel
```

Run:
```
docker-compose up
```

