import json
import os
import sys
from src.commands import add_task, list_tasks, complete_task, delete_task

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

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"No task with id {task_id}")
        return
    # Reassign ids (optional)
    for idx, t in enumerate(new_tasks, start=1):
        t["id"] = idx
    save_tasks(new_tasks)
    print(f"Deleted task {task_id}")

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
        desc = " ".join(sys.argv[2:])
        t = add_task(desc)
        print(f"Added task {t['id']}: {t['description']}")
    elif command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks yet.")
        else:
            for t in tasks:
                status = "✔" if t["completed"] else " "
                print(f"[{t['id']}] [{status}] {t['description']}")
    elif command == "complete" and len(sys.argv) == 3:
        try:
            tid = int(sys.argv[2])
            ok = complete_task(tid)
            if ok:
                print(f"Task {tid} marked as completed")
            else:
                print(f"No task with id {tid}")
        except ValueError:
            print("Invalid task id")
    elif command == "delete" and len(sys.argv) == 3:
        try:
            tid = int(sys.argv[2])
            ok = delete_task(tid)
            if ok:
                print(f"Deleted task {tid}")
            else:
                print(f"No task with id {tid}")
        except ValueError:
            print("Invalid task id")
    else:
        print_usage()

if __name__ == "__main__":
    main()