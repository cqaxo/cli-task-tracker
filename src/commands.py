from .storage import load_tasks, save_tasks

def add_task(description):
    tasks = load_tasks()
    new_task = {"id": len(tasks) + 1, "description": description, "completed": False}
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def list_tasks():
    tasks = load_tasks()
    return tasks

def complete_task(task_id):
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            found = True
            break
    if not found:
        return False
    save_tasks(tasks)
    return True

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        return False
    # Reassign ids
    for idx, t in enumerate(new_tasks, start=1):
        t["id"] = idx
    save_tasks(new_tasks)
    return True
