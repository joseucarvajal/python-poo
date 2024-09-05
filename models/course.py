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
    _code:str #as private attribute
    _name: str #as private attribute
    start_date: datetime
    end_date: datetime 
    _cut1_percentaje: float #as private attribute
    _cut2_percentaje: float #as private attribute
    _cut3_percentaje: float #as private attribute

    #encapsulation:
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value: str):
        trimmed_value = value.strip() if value is not None else value
        if not trimmed_value or len(trimmed_value) == 0:
            raise ValueError("code cannot be empty")
        self._code = trimmed_value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        trimmed_value = value.strip() if value is not None else value
        if not trimmed_value or len(trimmed_value) == 0:
            raise ValueError("name cannot be empty")
        self._name = trimmed_value

    @property
    def cut1_percentaje(self):
        return self._cut1_percentaje
    
    @cut1_percentaje.setter
    def cut1_percentaje(self, value: float):
        if value < 0:
            raise ValueError("cut 1 percentaje cannot be negative")
        self._cut1_percentaje = value

    @property
    def cut2_percentaje(self):
        return self._cut2_percentaje
    
    @cut2_percentaje.setter
    def cut2_percentaje(self, value: float):
        if value < 0:
            raise ValueError("cut 2 percentaje cannot be negative")
        self._cut2_percentaje = value

    @property
    def cut3_percentaje(self):
        return self._cut3_percentaje
    
    @cut3_percentaje.setter
    def cut3_percentaje(self, value: float):
        if value < 0:
            raise ValueError("cut 3 percentaje cannot be negative")
        self._cut3_percentaje = value
    
    #Methods
    def are_cuts_valid(self):
        if self.cut1_percentaje + self.cut2_percentaje + self.cut3_percentaje != 100:
            raise ValueError("The cuts percentaje should not be different than 100")

    def are_dates_valid(self):
        if self.start_date > self.end_date:
            #Error handling
            raise ValueError("The start date should be lesser than the end date")