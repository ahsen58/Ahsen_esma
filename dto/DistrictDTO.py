from dto.BaseDTO import BaseDTO


class DistrictDTO(BaseDTO):
    def __init__(self,district_id,city_id,name,code):
        BaseDTO.__init__(self, district_id)
        self.city_id = city_id
        self.name = name
        self.code = code
