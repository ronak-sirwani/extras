import time

class lift:
    baseFloor=0
    highestFloor=3

    def __init__(self,intial) -> None:
        self.currFloor= intial
        # lift speed is in floor/sec
        self.liftSpeed= 0.2

    
    def moveUp(self,floor):
        #s1= "lift is moving up to "+ str(floor)
        s2= self.reach(floor, distance= floor-self.currFloor)
        return s2
        
    def moveDown(self,floor):
        #s1= "lift is moving down to "+ str(floor)
        s2= self.reach(floor,distance= self.currFloor-floor)
        return s2

    def doSomething(self):
        return "Lift at floor : "+str(self.currFloor)
    
    def reach(self,floor,distance):
        required_time= distance/self.liftSpeed
        self.f=0
        c=0
        while required_time>0:
            c+= 0.2
            print(c)
            if self.f==1:
                return "EMERGENCY STOP !"
            if required_time>1:
                time.sleep(1)
                required_time-=1
            else:
                time.sleep(required_time)
                required_time=0
        if self.f==0:
            self.currFloor= floor
            return "Floor "+str(floor)+"reached"
    
    def Stop(self,stop=None):
        self.f=1
        if stop:
            return "stopped"
        else:
            return "fine"
    