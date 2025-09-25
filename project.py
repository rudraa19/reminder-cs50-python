from datetime import date
from backend.app.database.connection import init_db, session
from backend.app.models.task import Task as TaskModel

init_db()

def main():
    print("Welcome to Reminder App!")
    print("1. Create Task\n2. Get Task\n3. Update Task\n4. Delete Task")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Task title: ")
        desc = input("Task description: ")
        due = input("Due date (YYYY-MM-DD): ")
        task = create_task(title, desc, date.fromisoformat(due))
        print(f"Task created: {task}")
    elif choice == "2":
        task_id = int(input("Task ID: "))
        task = get_task(task_id)
        print(task)
    elif choice == "3":
        task_id = int(input("Task ID: "))
        title = input("New title: ")
        desc = input("New description: ")
        due = input("New due date (YYYY-MM-DD): ")
        completed = input("Is completed? (y/n): ").lower() == "y"
        task = update_task(task_id, title, desc, date.fromisoformat(due), completed)
        print(f"Task updated: {task}")
    elif choice == "4":
        task_id = int(input("Task ID: "))
        delete_task(task_id)
        print("Task deleted.")
    else:
        print("Invalid choice.")

def create_task(title: str, desc: str, due_date: date, is_completed: bool = False):
    db = session()
    task = TaskModel(title=title, desc=desc, due_date=due_date, is_completed=is_completed)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return {"id": task.id, "title": task.title, "desc": task.desc, "due_date": str(task.due_date), "is_completed": task.is_completed}

def get_task(task_id: int):
    db = session()
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    db.close()
    if not task:
        return {"error": "Task not found"}
    return {"id": task.id, "title": task.title, "desc": task.desc, "due_date": str(task.due_date), "is_completed": task.is_completed}

def update_task(task_id: int, title: str, desc: str, due_date: date, is_completed: bool):
    db = session()
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        db.close()
        return {"error": "Task not found"}
    task.title = title
    task.desc = desc
    task.due_date = due_date
    task.is_completed = is_completed
    db.commit()
    db.refresh(task)
    db.close()
    return {"id": task.id, "title": task.title, "desc": task.desc, "due_date": str(task.due_date), "is_completed": task.is_completed}

def delete_task(task_id: int):
    db = session()
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        db.close()
        return {"error": "Task not found"}
    db.delete(task)
    db.commit()
    db.close()
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    main()
