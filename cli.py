import json
import os
import sys

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added task {new_task['id']}: {description}")

def print_usage():
    print("Usage:")
    print("  python cli.py add <description>")
    print("  python cli.py list")
    print("  python cli.py complete <id>")
    print("  python cli.py delete <id>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) >= 3:
        description = " ".join(sys.argv[2:])
        add_task(description)
    else:
        print_usage()

if __name__ == "__main__":
    main()
