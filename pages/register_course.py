import streamlit as st

from models.course import Course


# Store a session variable
if 'courses_list' not in st.session_state:
    st.session_state.courses_list = []

st.title("Register course")

col1, col2 = st.columns(2)
with col1:
    code_input = st.text_input(label="Course code")
    start_date_input = st.date_input(label="Start date")

with col2:
    name_input = st.text_input(label="Course name")
    end_date_input = st.date_input(label="End date")

col1, col2, col3 = st.columns(3)
with col1:
    cut1_percentaje_input = st.number_input(label="% cut 1")
with col2:
    cut2_percentaje_input = st.number_input(label="% cut 2")
with col3:
    cut3_percentaje_input = st.number_input(label="% cut 3")

if st.button("Save course"):
    try:    
        #objects
        course = Course(
            code=code_input,
            name=name_input,
            start_date=start_date_input,
            end_date=end_date_input,
            cut1_percentaje=cut1_percentaje_input,
            cut2_percentaje=cut2_percentaje_input,
            cut3_percentaje=cut3_percentaje_input,
        )
        st.write(course)
        st.session_state.courses_list.append(course)
    except ValueError as e:
        st.error(e)