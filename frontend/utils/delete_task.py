import requests
from config import BACKEND_URL
import streamlit as st

def delete_task(task_id):
    try:
        requests.delete(f"{BACKEND_URL}/tasks/{task_id}")
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting tasks: {e}")
        return
