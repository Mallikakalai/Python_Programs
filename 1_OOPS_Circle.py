#create a python class circle with constructor which will take a list as an argument for the task. 
#The list is [10, 501, 22, 37, 100, 999, 87, 351], from the given list create 2 class methods Area & Perimeter which will be going to calculate the area and perimeter

#created a class circle with constructor that takes a list as an argument
class circle:
    
    def __init__(self,radiuslist):
        self.radiuslist=radiuslist

    def area(self):
        pi=3.141
        areaofcircle=[2*pi*r*r for r in self.radiuslist] 
        print("Area of the Circle", areaofcircle)
    
    def perimeter(self):
        pi=3.141
        perimeterofcircle=[2*pi*r for r in self.radiuslist]
        print("Perimeter of the Circle", perimeterofcircle)

radiuslist=[10, 501, 22, 37, 100, 999, 87, 351]
objcircle=circle(radiuslist) #created object and passing list as an argument
objcircle.area() 
objcircle.perimeter() 