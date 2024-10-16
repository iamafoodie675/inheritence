class vehicle:
    def __init__(self,name, max_speed,mileage,capacity):
        self.name =name
        self.max_speed =max_speed
        self.mileage=mileage
        self.capacity =capacity
        
    def fare(self):
        return self.capacity*100
    
class bus(vehicle):
    def fare(self):
        amount = super().fare()
        amount =amount +((amount* 10)/100)
        
        return amount
    
schoolbus = bus("school volvo",180,12,50)
print(f"vehicle name:{schoolbus.name}\nspeed:{schoolbus.max_speed}\nmileage:{schoolbus.mileage}")
print(f"\nbus fare: {schoolbus.fare()}")
        
        
        