import requests
from config import BACKEND_URL
import streamlit as st

def get_tasks():
    try:
        tasks = requests.get(f"{BACKEND_URL}/tasks")
        return tasks.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching tasks: {e}")
        return []
