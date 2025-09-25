import streamlit as st

st.set_page_config(page_title="Task Details")
st.title("📄 Task Details")

task_id = st.query_params["task_id"]

st.write(f"Task desc for {task_id}")