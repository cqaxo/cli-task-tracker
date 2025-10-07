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

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "✔" if t["completed"] else " "
        print(f"[{t['id']}] [{status}] {t['description']}")

def complete_task(task_id):
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            found = True
            break
    if not found:
        print(f"No task with id {task_id}")
        return
    save_tasks(tasks)
    print(f"Task {task_id} marked as completed")

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
    elif command == "list":
        list_tasks()
    elif command == "complete" and len(sys.argv) == 3:
        try:
            tid = int(sys.argv[2])
            complete_task(tid)
        except ValueError:
            print("Invalid task id")
    else:
        print_usage()

if __name__ == "__main__":
    main()
