import streamlit as st

from functools import reduce

from models.course import Course
from models.vacations_course import VacationsCourse
from models.free_course import FreeCourse


# Store a session variable
if 'courses_list' not in st.session_state:
    st.session_state.courses_list = []

st.title("Register course")

col1, col2 = st.columns(2)
with col1:
    code_input = st.text_input(label="Course code")
    start_date_input = st.date_input(label="Start date")
    price_input = st.number_input(label="Price")

with col2:
    name_input = st.text_input(label="Course name")
    end_date_input = st.date_input(label="End date")
    course_type = st.selectbox(label="Choose a course", options=["Academic", "Vacations course", "Free course"])

col1, col2, col3 = st.columns(3)
with col1:
    cut1_percentaje_input = st.number_input(label="% cut 1", value=30)
with col2:
    cut2_percentaje_input = st.number_input(label="% cut 2", value=35)
with col3:
    cut3_percentaje_input = st.number_input(label="% cut 3", value=35)

if st.button("Save course"):
    try:   
        course = None 
        if course_type == "Academic":
            #objects
            course = Course(
                code=code_input,
                name=name_input,
                start_date=start_date_input,
                end_date=end_date_input,
                cut1_percentaje=cut1_percentaje_input,
                cut2_percentaje=cut2_percentaje_input,
                cut3_percentaje=cut3_percentaje_input,
                price=price_input
            )
        elif course_type == "Vacations course":
            course = VacationsCourse(
                code=code_input,
                name=name_input,
                start_date=start_date_input,
                end_date=end_date_input,
                cut1_percentaje=cut1_percentaje_input,
                cut2_percentaje=cut2_percentaje_input,
                cut3_percentaje=cut3_percentaje_input,
                price=price_input
            )
        else:
            course = FreeCourse(
                code=code_input,
                name=name_input,
                start_date=start_date_input,
                end_date=end_date_input,
                cut1_percentaje=cut1_percentaje_input,
                cut2_percentaje=cut2_percentaje_input,
                cut3_percentaje=cut3_percentaje_input,
                price=price_input
            )

        st.write("Course info", vars(course))

        #polimorphism
        st.session_state.courses_list.append(course)
        def sum_final_prices(total: float, course: Course) -> float:
            return total + course.get_final_price()
                            
        total_price = reduce(sum_final_prices, st.session_state.courses_list, 0)

        st.success(f"Total price: {total_price}")

    except ValueError as e:
        st.error(e)