class WorkAnalysis:
    def __init__(self, data):
        self.data = data
        self.toplam = len(data)

    def working_percentage(self):
        if self.toplam == 0:
            return 0.0
        calisan = sum(1 for k in self.data if k.is_working == 1)
        return round((calisan / self.toplam) * 100, 2)