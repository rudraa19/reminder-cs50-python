import requests
from config import BACKEND_URL
import streamlit as st

def create_task(title, desc, due_date, is_completed):

    data = {
        "title": title,
        "desc": desc,
        "due_date": due_date,
        "is_completed": is_completed
    }

    try:
        tasks = requests.post(f"{BACKEND_URL}/tasks", json=data)
        return tasks.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating task: {e}")
        return []
