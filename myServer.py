import cherrypy
from simplemachine import lift
from moving import Move
import time

class server(object):
    def __init__(self) -> None:
        self.f=0
        self.mylist= lift(intial=0)

    @cherrypy.expose
    def index(self):
        s= "<a href=http://127.0.0.1:10001/moveMachine?>Click Here TO START THE MACHINE</a>"
        return s
    
    @cherrypy.expose
    def moveMachine(self,moveTo=None):
        #print(self.mylist.currFloor)
        print(Move.decideMove(self.mylist,moveTo))
    
    @cherrypy.expose
    def emergencyStop(self,stop):
        return self.mylist.Stop(stop)
                

    @cherrypy.expose
    def stopMachine(self):
        self.f=1 
        print("FSM stopped !")

        cherrypy.engine.exit()


    

if __name__ == '__main__':
    cherrypy.config.update({"server.socket_port":10001})
    cherrypy.quickstart(server())