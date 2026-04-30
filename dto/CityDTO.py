from dto.BaseDTO import BaseDTO


class CityDTO(BaseDTO) :
    def __init__(self,city_id,country_id,name,code):
        BaseDTO.__init__(self, city_id)
        self.country_id = country_id
        self.name = name
        self.code = code