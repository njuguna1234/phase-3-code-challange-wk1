class Car:
    
    def __init__(self, make, model, year):  
        self.make = make    
        self.model = model  
        self.year = year    
    
    
    def display_info(self):  
        
        print(f"Car Make: {self.make}, Car Model: {self.model}, Car Year: {self.year}")


my_car = Car("Mazda", "Demio", 2021)  


my_car.display_info()
