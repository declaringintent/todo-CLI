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
# list all tasks
python todo.py list
# list only done tasks
python todo.py list done
# change the status of a task
python todo.py done 1
# delete a task
python todo.py delete 1
# search a keyword
python todo.py search "milk"
# update a task
python todo.py update 1 "add milk and exercise"
