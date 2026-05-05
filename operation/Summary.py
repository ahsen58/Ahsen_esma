class PopulationSummary:
    def __init__(self, data):
        self.data = data

    def total_population(self):
        return len(self.data)

    def summary(self):
        return {"Toplam Kişi": self.total_population()}