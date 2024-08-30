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


