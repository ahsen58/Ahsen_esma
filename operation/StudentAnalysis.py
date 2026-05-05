class StudentAnalysis:
    def __init__(self, data):
        self.data = data
        self.toplam = len(data)

    def student_percentage(self):
        if self.toplam == 0:
            return 0.0
        ogrenci = sum(1 for k in self.data if k.is_student == 1)
        return round((ogrenci / self.toplam) * 100, 2)