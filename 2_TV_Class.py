# Question - https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md
class TV:
    
    def __init__(self,brand):
        self.brand=brand
        self.channel=1
        self.price=None
        self.inches=None
        self.OnOff=None
        self.volume=50

    def incvolume(self):
        if self.volume<100:
            self.volume=self.volume+1
    
    def decvolume(self):
        if self.volume>0:
            self.volume=self.volume-1
    
    def setchannel(self,channel):
            if 1 <= channel <= 50:
                self.channel=channel
    
    def reset(self):
        self.channel=1
        self.volume=50
    
    def TVstatus(self):
        print (self.brand," at channel ",self.channel," volume ",self.volume)
    
class LED(TV):
    def __init__(self,brand,screenthickness, energyusage,lifespan, refreshrate,Backlight,viewingAngle):
            super().__init__(brand)
            self.screenthickness=screenthickness
            self.energyusage=energyusage
            self.lifespan=lifespan
            self.refreshrate=refreshrate
            self.Backlight=Backlight
            self.viewingAngle=viewingAngle

    def DisplayDetails(self):
            print("LET TV Propertites & Functionalities ","\n","Screen Thickness: ",self.screenthickness,"mm","\n","Energy Usage: ",self.energyusage,"star","\n","Life Span: ",self.lifespan,"years","\n","Refresh Rate:",self.refreshrate,"Hz","\n","Viewing Angle",self.viewingAngle,"Degree","\n","Backlight:",self.Backlight)

class Plasma(TV):
        def __init__(self,brand,screenthickness, energyusage,lifespan, refreshrate,Backlight,viewingAngle):
            super().__init__(brand)
            self.screenthickness=screenthickness
            self.energyusage=energyusage
            self.lifespan=lifespan
            self.refreshrate=refreshrate
            self.Backlight=Backlight
            self.viewingAngle=viewingAngle

        def DisplayDetails(self):
            print("Plasma TV Propertites & Functionalities ","\n","Screen Thickness: ",self.screenthickness,"mm","\n","Energy Usage: ",self.energyusage,"star","\n","Life Span: ",self.lifespan,"years","\n","Refresh Rate:",self.refreshrate,"Hz","\n","Viewing Angle",self.viewingAngle,"Degree","\n","Backlight:",self.Backlight)

ObjTV=TV("TCL")
ObjLEDTV = LED("Sony",8,3,10,120,"Available",180)
ObjPlasmaTV = Plasma("Panasonic",20,5,15,60,"Not Available",120)

ObjTV.TVstatus()
ObjTV.incvolume()
ObjTV.setchannel(34)
ObjTV.TVstatus()
ObjTV.setchannel(78) #since this channel is not available it will remain in the same channel
ObjTV.decvolume()
ObjTV.TVstatus()
ObjTV.reset()
ObjTV.TVstatus()
ObjLEDTV.DisplayDetails()
ObjPlasmaTV.DisplayDetails()



