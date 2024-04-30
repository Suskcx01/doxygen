class Car:
    def __init__(self, name, model, color, year):
        self.name = name
        self.model = model
        self.color = color
        self.year = year

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")

# Example usage
car1 = Car("Toyota", "Corolla", "Red", 2020)
car1.display_info()
