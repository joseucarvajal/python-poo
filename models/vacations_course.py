from .course import Course


class VacationsCourse(Course):
    def __init__(
            self, 
            code, 
            name, 
            start_date, 
            end_date, 
            cut1_percentaje, 
            cut2_percentaje, 
            cut3_percentaje, 
            price):
        super().__init__(code, name, start_date, end_date, cut1_percentaje, cut2_percentaje, cut3_percentaje, price)

    def get_final_price(self):
        return self.price * 1.10


