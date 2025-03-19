class Smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def get_info(self):
        return f"{self.brand} - {self.model}. {self.number}"
