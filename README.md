# Simple Python Todo CLI

A minimal command-line todo list app built with Python. Tasks are saved to a `todos/todos.json` file and persist between runs.

## Features

- Add new tasks
- Toggle task status (done / not done)
- Delete tasks
- Automatic JSON file saving
- Creates a `todos/` folder on first run

## Getting Started

Make sure you have **Python 3.7+** installed.

Run the app with:

```bash
python to_do.py
```

## Available Commands
Type a task description → adds a new todo

done N → toggle task #N as done/undone

del N → delete task #N

exit → exit the program

#### Example Usage
```bash
> buy milk
> walk the dog
> done 1
> del 2
> exit
```

## Data Format
Tasks are stored as a list of objects:

json
Копіювати
Редагувати
[
  {
    "task": "buy milk",
    "done": true
  },
  {
    "task": "walk the dog",
    "done": false
  }
]