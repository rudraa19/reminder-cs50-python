import streamlit as st
from utils.get_task import get_task
from utils.update_task import update_task

st.set_page_config(page_title="Task Details")
st.title("📄 Task Details")

task_id = st.query_params["task_id"]

task = get_task(task_id)

st.markdown("---")

st.markdown(
    """
    <a href="./">&larr; Back</a>
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


delete_html = """
<div class="delete-button">
    <button>Delete task</button>
</div>
<style>
.delete-button button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 5px;
    padding: 0.5em 1em;
    font-weight: bold;
    border: none;
}
.delete-button button:hover {
    background-color: #ff1a1a;
    color: white;
}
</style>
"""

st.markdown(delete_html, unsafe_allow_html=True)