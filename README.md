# CLI Task Manager

A simple command-line interface (CLI) task manager that allows users to add, delete, and list tasks. Tasks are stored in a JSON file (`tasks.json`), making it easy to manage your to-do list.

## Features

- Add new tasks with a title and priority (low, medium, high).
- Delete tasks by their ID.
- List all current tasks with their details.

## Requirements

- Python 3.x
- No external libraries are required (uses built-in `argparse` and `json` modules).

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3 installed on your machine.
3. Navigate to the directory containing the script.

## Usage

You can use the task manager by running the script from the command line. The following commands are available:

### Add, Delete, and List a Task

- To add a new task, use the `add` command followed by the task title. You can also specify the priority (default is medium).
- To delete a task, use the delete command followed by the task ID.
- To list all tasks, use the list command.

```bash
python task_manager.py add "Your Task Title" --priority high
python task_manager.py delete 1
python task_manager.py list
