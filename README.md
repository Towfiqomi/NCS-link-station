# NCS-link-station

The project can be run with or without the Docker. No need to create any virtual environment as Poetry will isolate the dependencies and create a venv by itself. Docker images can be built and run using the Makefile commands.

#### With Docker

Use the follwing command in root folder where the `Makefile` is,
```bash
make up
```

To stop the container use the command,
```bash
make down
```

#### Without the Docker

To run the API first install Poetry,

```bash
pip install --upgrade pip 'poetry==1.1.5'
```

Required dependencies are added in `pyproject.toml`. To install the dependencies, Run the following command,
```bash
poetry install --no-root
```
Now to run the application,
```bash
poetry run uvicorn apis.main:app --host 0.0.0.0 --port 3000 --reload
```


### The Swagger URLS

- [API Docs](http://localhost:3000/docs)
- [API Redoc](http://localhost:3000/redoc)
