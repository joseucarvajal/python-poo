import datetime

#Class
class Course:

    #Constructor method
    def __init__(self, code, name, start_date, end_date, cut1_percentaje, cut2_percentaje, cut3_percentaje):
        self.code = code
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.cut1_percentaje = cut1_percentaje
        self.cut2_percentaje = cut2_percentaje
        self.cut3_percentaje = cut3_percentaje
        self.are_cuts_valid()
        self.are_dates_valid()

    #Attributes
    code:str
    name: str
    start_date: datetime
    end_date: datetime
    cut1_percentaje: float
    cut2_percentaje: float
    cut3_percentaje: float

    #Methods
    def are_cuts_valid(self):
        if self.cut1_percentaje + self.cut2_percentaje + self.cut3_percentaje != 100:
            raise ValueError("The cuts percentaje should not be different than 100")

    def are_dates_valid(self):
        if self.start_date >= self.end_date:
            #Error handling
            raise ValueError("The start date should be lesser than the end date")
        
    