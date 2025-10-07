import sys
from src.commands import add_task, list_tasks, complete_task, delete_task

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
        t = add_task(desc)  # returns dict from src.commands
        print(f"Added task {t['id']}: {t['description']}")
    elif command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks yet.")
        else:
            for task in tasks:
                status = "✔" if task["completed"] else " "
                print(f"[{task['id']}] [{status}] {task['description']}")
    elif command == "complete" and len(sys.argv) == 3:
        try:
            tid = int(sys.argv[2])
            print(
                f"Task {tid} marked as completed"
                if complete_task(tid)
                else f"No task with id {tid}"
            )
        except ValueError:
            print("Invalid task id")
    elif command == "delete" and len(sys.argv) == 3:
        try:
            tid = int(sys.argv[2])
            print(
                f"Deleted task {tid}"
                if delete_task(tid)
                else f"No task with id {tid}"
            )
        except ValueError:
            print("Invalid task id")
    else:
        print_usage()

if __name__ == "__main__":
    main()
