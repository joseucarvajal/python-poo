from models.course import Course


class Student:
    code:str
    name:str
    emails:str
    courses_list: list[Course]

    def __init__(self, code, name, emails) -> None:
        self.code = code
        self.name = name
        self.emails = emails

    def add_course(self, course: Course):
        self.courses_list.append(course)
