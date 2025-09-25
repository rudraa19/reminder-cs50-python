import streamlit as st
from utils.get_tasks import get_tasks
from utils.create_task import create_task

st.set_page_config(page_title="Reminder App")
st.title("📝 Reminder App")

st.markdown("---")

with st.expander("Add New Task"):
    with st.form(key="add_task_form"):
        title = st.text_input("Task Title")
        desc = st.text_area("Task Description")
        due_date = st.date_input("Due Date")
        is_completed = st.checkbox("Completed")
        submit = st.form_submit_button("Add Task")
   
    if submit:
        new_task = {
            "title": title,
            "desc": desc,
            "due_date": due_date.strftime("%Y-%m-%d"),
            "is_completed": is_completed
        }
        create_task(
            title=new_task["title"],
            desc=new_task["desc"],
            due_date=new_task["due_date"],
            is_completed=new_task["is_completed"]
        )
        st.session_state.tasks = get_tasks()
        st.success("Task added successfully!")


if "tasks" not in st.session_state:
    st.session_state.tasks = get_tasks()

tasks = st.session_state.tasks

if tasks:
    col2, col3, col4, col5 = st.columns([3, 2, 1, 1])
    col2.write("Title")
    col3.write("Due Date")
    col4.write("Completed")
    col5.write("Details")

    for task in tasks:
        col2, col3, col4, col5 = st.columns([3, 2, 1, 1])
        col2.write(task["title"])
        col3.write(task["due_date"])
        col4.write("✅" if task["is_completed"] else "❌")
        col5.markdown(
            f'<a href="./task_details?task_id={task["id"]}" target="_self">View</a>',
            unsafe_allow_html=True
        )
else:
    st.info("No tasks yet!")
