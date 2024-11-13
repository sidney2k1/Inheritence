class vehicle:
    def __init__(self,name,mileage,capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity
    def fare(self):
        return self.capacity*100
class bus(vehicle):
    def fare(self):
        amount=super().fare()
        amount+=amount*10/100
        return amount
schoolbus=bus("School volvo",12,50)
print("Total bus fare is:",schoolbus.fare())