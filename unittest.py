class Vehicle:
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
  
   def vehicle_info(self):
       return f"{self.year} {self.make} {self.model}"


class ElectricCar(Vehicle):
   def __init__(self, make, model, year, battery_capacity, current_charge):
       super().__init__(make, model, year)
       self.battery_capacity = battery_capacity  # in kWh
       self.current_charge = current_charge  # in kWh
  
   def calculate_range(self):
       average_consumption = 0.2  # kWh per mile, for simplicity
       return (self.current_charge / average_consumption)
import unittest


class TestElectricCar(unittest.TestCase):
  
   def test_calculate_range_full_charge(self):
       car = ElectricCar("Tesla", "Model S", 2022, 100, 100)
       self.assertEqual(car.calculate_range(), 500)
  
   def test_calculate_range_partial_charge(self):
       car = ElectricCar("Tesla", "Model 3", 2023, 75, 30)
       self.assertEqual(car.calculate_range(), 150)


if __name__ == '__main__':
   unittest.main()

#code added by the contributor

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y 

class Testcalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()
#comment 