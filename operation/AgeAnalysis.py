class AgeAnalysis:
    def __init__(self, data):
        self.data = data
        self.toplam = len(data)

    def average_age(self):
        if self.toplam == 0:
            return 0.0
        return round(sum(k.age for k in self.data) / self.toplam, 1)

    def min_max_age(self):
        if self.toplam == 0:
            return {"En Genç": 0, "En Yaşlı": 0}
        return {
            "En Genç": min(k.age for k in self.data),
            "En Yaşlı": max(k.age for k in self.data)
        }

    def age_groups(self):
        gruplar = {"0-17": 0, "18-35": 0, "36-60": 0, "60+": 0}
        for k in self.data:
            if k.age < 18:
                gruplar["0-17"] += 1
            elif k.age <= 35:
                gruplar["18-35"] += 1
            elif k.age <= 60:
                gruplar["36-60"] += 1
            else:
                gruplar["60+"] += 1
        return gruplar