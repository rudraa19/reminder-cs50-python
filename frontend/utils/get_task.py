import requests
from config import BACKEND_URL
import streamlit as st

def get_task(task_id):
    try:
        tasks = requests.get(f"{BACKEND_URL}/tasks/{task_id}")
        return tasks.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching task: {e}")
        return []
