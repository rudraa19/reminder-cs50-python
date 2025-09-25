# test_project.py
from datetime import date
from project import create_task, get_task, update_task, delete_task

def test_create_task():
    task = create_task("Test Task", "This is a test", date(2025, 1, 1))
    assert task["title"] == "Test Task"
    assert task["desc"] == "This is a test"

def test_get_task():
    task = create_task("Get Task", "Get test", date(2025, 1, 2))
    fetched = get_task(task["id"])
    assert fetched["id"] == task["id"]

def test_update_task():
    task = create_task("Update Task", "Update test", date(2025, 1, 3))
    updated = update_task(task["id"], "Updated Title", "Updated desc", date(2025, 1, 4), True)
    assert updated["title"] == "Updated Title"
    assert updated["is_completed"] is True

def test_delete_task():
    task = create_task("Delete Task", "Delete test", date(2025, 1, 5))
    result = delete_task(task["id"])
    assert result["message"] == "Task deleted successfully"
