class vehicle:
    def __init__(self,name,mileage,maxspeed):
        self.name=name
        self.mileage=mileage
        self.maxspeed=maxspeed
class bus(vehicle):
    pass
Schoolbus=bus("School volvo",12,180)
print("Vehicle Name:",Schoolbus.name,"Mileage",Schoolbus.mileage,"Speed",Schoolbus.maxspeed)