import cherrypy
from temp1 import makeBoolean

class Variable(object):
    def __init__(self) -> None:
        self.obj= makeBoolean()

    @cherrypy.expose
    def index(self):
        return "connection established"
    
    @cherrypy.expose
    def changeVariable(self,b):
        return self.obj.changeVar(b)

if __name__ == '__main__':
    cherrypy.config.update({"server.socket_port":10005})
    cherrypy.quickstart(Variable())