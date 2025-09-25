import streamlit as st
import pandas as pd
from config import BACKEND_URL

st.set_page_config(page_title="Reminder App")
st.title("📝 Reminder App")

# Sample tasks
def get_tasks():
    return [
        {"id": 1, "title": "Buy groceries", "desc": "Milk, Eggs, Bread", "due_date": "2025-09-30", "is_completed": False},
        {"id": 2, "title": "Call Mom", "desc": "Check in and chat", "due_date": "2025-09-26", "is_completed": True},
    ]

with st.expander("Add New Task"):
    with st.form(key="add_task_form"):
        title = st.text_input("Task Title")
        desc = st.text_area("Task Description")
        due_date = st.date_input("Due Date")
        is_completed = st.checkbox("Completed")
        submit = st.form_submit_button("Add Task")

        if submit:
            new_task = {
                "id": len(st.session_state.tasks) + 1,
                "title": title,
                "desc": desc,
                "due_date": due_date.strftime("%Y-%m-%d"),
                "is_completed": is_completed
            }
            st.session_state.tasks.append(new_task)
            st.success(f"Task '{title}' added successfully!")
            st.rerun()

if "tasks" not in st.session_state:
    st.session_state.tasks = get_tasks()

tasks = st.session_state.tasks

if tasks:
    col1, col2, col3, col4, col5 = st.columns([1, 3, 2, 1, 1])
    col1.write("ID")
    col2.write("Title")
    col3.write("Due Date")
    col4.write("Completed")
    col5.write("Details")

    for task in tasks:
        col1, col2, col3, col4, col5 = st.columns([1, 3, 2, 1, 1])
        col1.write(task["id"])
        col2.write(task["title"])
        col3.write(task["due_date"])
        col4.write("✅" if task["is_completed"] else "❌")
        col5.markdown(
            f'<a href="./task_details?task_id={task["id"]}" target="_self">View</a>',
            unsafe_allow_html=True
        )
else:
    st.info("No tasks yet!")
