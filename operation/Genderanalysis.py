class GenderAnalysis:
    def __init__(self, data):
        self.data = data
        self.toplam = len(data)

    def calculate(self):
        if self.toplam == 0:
            return {"Kadın": 0.0, "Erkek": 0.0, "Diğer": 0.0}
        kadin = sum(1 for k in self.data if k.gender == "Kadın")
        erkek = sum(1 for k in self.data if k.gender == "Erkek")
        diger = self.toplam - kadin - erkek
        return {
            "Kadın": round((kadin / self.toplam) * 100, 2),
            "Erkek": round((erkek / self.toplam) * 100, 2),
            "Diğer": round((diger / self.toplam) * 100, 2)
        }