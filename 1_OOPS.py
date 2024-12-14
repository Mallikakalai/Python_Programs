#create a python class circle with constructor which will take a list as an argument for the task. 
#The list is [10, 501, 22, 37, 100, 999, 87, 351]
#from the given list create 2 class methods Area & Perimeter which will be going to calculate the area and perimeter

#created a class circle with constructor that takes a list as an argument
class circle:
    def __init__(self,radius):
        self.radius=radius

#created a class method area to calculate the area of the circle (pi*r*r)
    def area(self):
        pi=3.141
        print("Area of the Circle of radius ",self.radius, "is", self.radius**2*pi)
    

#created a class method area to calculate the perimeter of the circle (2*pi*r)
    def perimeter(self):
        pi=3.141
        print("Perimeter of the Circle of radius ",self.radius, "is", self.radius*2*pi)

radiuslist=[10, 501, 22, 37, 100, 999, 87, 351]
for i in radiuslist:
    objcircle=circle(i)
    objcircle.area()
    objcircle.perimeter()



