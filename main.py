class Avto:
    def __init__(self, model, rang, korobka, narh, firma, km):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.firma = firma
        self.km = 400

    def get_model(self):
        return f"{self.model}"

    def get_rang(self):
        return f"{self.rang}"

    def get_korobka(self):
        return f"{self.korobka}"

    def get_summa(self):
        return f"{self.narh}"

    def get_km(self):
        return f"{self.km}"

    def get_firma(self):
        return f"{self.firma}"

    def get_full_avto(self):
        return f"{self.model} {self.rang} {self.korobka} {self.narh} {self.firma} {self.km}"

    def update_km(self):
        self.km += 400


Avto = Avto(f" Model:M5", " Color:Black", "Box:Mexanika", 2000, "BMW", 4000)
print(Avto.get_full_avto())
print(Avto.update_km())
print(Avto.get_full_avto())
