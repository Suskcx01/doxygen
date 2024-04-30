class Car:
    """
    A class representing a car.

    Attributes:
        name (str): The name of the car manufacturer.
        model (str): The model of the car.
        color (str): The color of the car.
        year (int): The manufacturing year of the car.

    Methods:
        display_info(): Display information about the car.
    """

    def __init__(self, name, model, color, year):
        """
        Initializes a new Car object.

        Args:
            name (str): The name of the car manufacturer.
            model (str): The model of the car.
            color (str): The color of the car.
            year (int): The manufacturing year of the car.
        """
        self.name = name
        self.model = model
        self.color = color
        self.year = year

    def display_info(self):
        """
        Display information about the car.
        """
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")

# Example usage
car1 = Car("Toyota", "Corolla", "Red", 2020)
car1.display_info()
