"""
A vehicle is identified by its mileage (in kms per litre) and fuel left (in litres) in the vehicle. From the fuel left, 5 litres will always be considered as reserve fuel. At any point of time, the driver of the vehicle may want to know:

the maximum distance that can be covered without using the reserve fuel
how many kms he/she has already travelled based on the initial fuel the vehicle had
"""

#!/python3
class Vehicle:
    def __init__(self):
        self.mileage=None
        self.fuel_left=None
    
    def identify_distance_travelled(self,initial_fuel):
        distance_travelled=(initial_fuel-self.fuel_left)* self.mileage
        return distance_travelled
    def identify_distance_that_can_be_travelled(self):
        initial_fuel=15
        distance_travelled=self.identify_distance_travelled(initial_fuel)
        if self.fuel_left>5:
            return (initial_fuel-5)*self.mileage- distance_travelled
        else:
            return 0
            
            
t = Vehicle()
t.mileage = 30
t.fuel_left  =10
print(t.mileage)
print(t.identify_distance_travelled(20))
print(t.identify_distance_that_can_be_travelled())
