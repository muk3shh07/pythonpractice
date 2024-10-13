class vechile:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        print(f"The make is {self.make} and model is {self.model}")
class car(vechile):
    def __init__(self, make, model , year):
        super().__init__(make, model)        
        self.year = year

    def get_info(self):
        super().get_info() 
        print(f"The year is {self.year}")

v1 = car(make="muke", model= "axc23", year = 2022)
v1.get_info()      

    