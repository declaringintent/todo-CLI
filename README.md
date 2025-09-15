# todo-cli

A small command-line TODO application implemented in Python. Good project to demonstrate CLI skills and basic file persistence.

## Features
- Add / list / update / delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- Search tasks by substring
- JSON persistence (`todo.json`)
- timestamps

## Install / Run
Requires Python 3.8+.

```bash
# run directly
python todo.py add "Buy milk"
python todo.py list
python todo.py done 1
