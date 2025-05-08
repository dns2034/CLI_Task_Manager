import argparse
import json

# attempts to read tasks from 'tasks.json'
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    # if the file does not exist, it reurns an empty list
    except FileNotFoundError:
        return []
    
# This takes a list of tasks and writes it to 'task.json' in JSON formatted structure
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

# this function adds a new task with a specified title and priority
# it loads existing tasks, assigns a new ID (incrementing from the last task's ID), appends the new task to the list, and saves the updated list back to the file
# then print the confirmation message
def add_task(title, priority="medium"):
    tasks = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": new_id, "title": title, "priority": priority})
    save_tasks(tasks)
    print(f"✅ Added task: '{title}' (Priority: {priority})")

# this function deletes a task by its ID
# it loads existing tasks, filters out the task with the specified ID, and saves the updated list
# if the task is not found, it prints an error message
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"❌ Task {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"🗑️ Deleted task {task_id}.")

# this function lists all tasks currently stored in 'task.json'
# if there are no tasks, it prints a message indicating that. Otherwise, it prints each task's ID, title, and priority
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("📝 Your Tasks:")
        for task in tasks:
            print(f"  {task['id']}. {task['title']} (Priority: {task['priority']})")


def main():
    # this function sets up the CLI using 'argparse'
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")
    add_parser.add_argument("--priority", choices=["low", "medium", "high"], default="medium")

    # Delete task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    # List tasks command
    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.priority)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "list":
        list_tasks()

if __name__ == "__main__":
    main()
