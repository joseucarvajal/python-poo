import datetime
from base.base_model import BaseModelWithRequiredString

#Class
class Course(BaseModelWithRequiredString):

    #Constructor method
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
        self.code = code
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.cut1_percentaje = cut1_percentaje 
        self.cut2_percentaje = cut2_percentaje
        self.cut3_percentaje = cut3_percentaje
        self.price = price
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
    _price: float

    #encapsulation:
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value: str):
        self._code = self.validate_req_str_value(property_name="code", value=value)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = self.validate_req_str_value(property_name="name", value=value)

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

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Prices cannot be a negative value")
        self._price = value
    
    #Methods
    def are_cuts_valid(self):
        if self.cut1_percentaje + self.cut2_percentaje + self.cut3_percentaje != 100:
            raise ValueError("The cuts percentaje should not be different than 100")

    def are_dates_valid(self):
        if self.start_date > self.end_date:
            #Error handling
            raise ValueError("The start date should be lesser than the end date")

    def get_final_price(self):
        return self.price
    