# Demyst Exercise

A command line tool that consumes the first 20 even numbered TODO's in most performant way and output the title and whether it is completed or not.

## Setup

**1. Install the requirements in requirements file.**

```shell
pip install -r requirements.txt
```

**3. Run the application**

```shell
python todo_cli.py
```

**4. Run the test cases**

```shell
python -m unittest test_todo_cli.py
```

**5. Build Docker file**

```shell
docker build -t todo-cli .
```

**6. Run the Docker file**

```shell
docker run --rm todo-cli
```