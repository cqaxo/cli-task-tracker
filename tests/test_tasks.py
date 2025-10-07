import os
from src.commands import add_task, list_tasks, complete_task, delete_task

TMP = "tasks.json"

import pytest

@pytest.fixture(autouse=True)
def clean_tasks_file():
    if os.path.exists(TMP):
        os.remove(TMP)
    yield
    if os.path.exists(TMP):
        os.remove(TMP)

def test_add_and_list():
    t = add_task("Test one")
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test one"

def test_complete_task():
    add_task("Test two")
    ok = complete_task(1)
    assert ok
    tasks = list_tasks()
    assert tasks[0]["completed"] == True

def test_delete_task():
    add_task("A")
    add_task("B")
    ok = delete_task(1)
    assert ok
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "B"
