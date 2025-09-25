import streamlit as st
from utils.get_task import get_task

st.set_page_config(page_title="Task Details")
st.title("📄 Task Details")

task_id = st.query_params["task_id"]

task = get_task(task_id)

with st.form(key="update_task_form"):
    title = st.text_input("Task Title", value=task["title"])
    desc = st.text_area("Task Description", value=task["desc"])
    due_date = st.date_input("Due Date", value=task["due_date"])
    is_completed = st.checkbox("Completed", value=task["is_completed"])
    submit = st.form_submit_button("Update Task")
    

st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        border: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff1a1a;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

delete = st.button("Delete task", )