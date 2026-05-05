from dto.BaseDTO import BaseDTO


class PopulationDTO(BaseDTO):
    def __init__(self, pop_id, country_id, city_id, district_id, age, gender, is_working, is_student):
        BaseDTO.__init__(self, pop_id)

        self.country_id = country_id
        self.city_id = city_id
        self.district_id = district_id
        self.age = age
        self.gender = gender
        self.is_working = is_working
        self.is_student = is_student