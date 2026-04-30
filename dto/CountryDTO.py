from dto.BaseDTO import BaseDTO


class CountryDTO(BaseDTO):
    def __init__(self,country_id,name, code):
        BaseDTO.__init__(self, country_id)
        self.name = name
        self.code = code