import requests
from config import BACKEND_URL
import streamlit as st

def update_task(title, desc, due_date, is_completed, task_id):

    data = {
        "id": task_id,
        "title": title,
        "desc": desc,
        "due_date": due_date,
        "is_completed": is_completed
    }

    try:
        tasks = requests.put(f"{BACKEND_URL}/tasks/{task_id}", json=data)
        return tasks.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating task: {e}")
        return
