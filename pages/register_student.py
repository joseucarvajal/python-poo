import streamlit as st

from models.course import Course
from models.student import Student

st.title("Register student")

student = None

col1, col2 = st.columns(2)
with col1:
    code_input = st.text_input(label="Code")
    name_input = st.text_input(label="Name")

with col2:
    emails_input = st.text_input(label="Emails")

if st.button("Save student"):
    try:    
        student = Student(
             code=code_input,
             name=name_input,
             emails=emails_input
        )
    except ValueError as e:
        st.error(e)

if student:
    st.header(f"Add course to student {student.name}")
    st.selectbox(label="Choose a course", options=[course.name for course in st.session_state.courses_list]
)