class BaseModelWithRequiredString:

    def validate_req_str_value(self, property_name:str, value:str):
        trimmed_value = value.strip() if value is not None else value
        if not trimmed_value or len(trimmed_value) == 0:
            raise ValueError(f"{property_name} cannot be empty") #Error hanbdling
        return trimmed_value
