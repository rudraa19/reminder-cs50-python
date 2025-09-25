import streamlit as st
from utils.get_task import get_task
from utils.update_task import update_task
from utils.delete_task import delete_task

def navigate(page_name):
    st.session_state.page = page_name

st.set_page_config(page_title="Task Details")
st.title("📄 Task Details")

hide_sidebar = """
    <style>
        /* Hide the sidebar */
        [data-testid="stSidebar"] {display: none;}
        /* Expand the main content to full width */
        [data-testid="stAppViewContainer"] {margin-left: 0;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)


task_id = st.query_params["task_id"]

task = get_task(task_id)

st.markdown("---")

st.markdown(
    """
    <a href="/" target="_self">&larr; Back</a>
    """,
    unsafe_allow_html=True
)

with st.form(key="update_task_form"):
    title = st.text_input("Task Title", value=task["title"])
    desc = st.text_area("Task Description", value=task["desc"])
    due_date = st.date_input("Due Date", value=task["due_date"])
    is_completed = st.checkbox("Completed", value=task["is_completed"])
    submit = st.form_submit_button("Update Task")

    if submit:
        updated_task = {
            "title": title,
            "desc": desc,
            "due_date": due_date.strftime("%Y-%m-%d"),
            "is_completed": is_completed
        }
        update_task(
            title=updated_task["title"],
            desc=updated_task["desc"],
            due_date=updated_task["due_date"],
            is_completed=updated_task["is_completed"],
            task_id=task_id
        )
        st.session_state.tasks = get_task(task_id)
        st.success("Task updated successfully!")

if st.button("Delete task"):
    if delete_task(task_id):
        st.success("Task deleted successfully!")
        st.markdown('You can now <a href="/" target="_self">Go back</a>', unsafe_allow_html=True)