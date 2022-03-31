#from simplemachine import lift

class Move():
    def decideMove(mylift,inp):
        #print("Current floor :",mylist.currFloor)
        if inp is None:
            return mylift.doSomething()
        elif int(inp) >= mylift.baseFloor and int(inp) <= mylift.highestFloor:
            #print(mylift.currFloor)
            if int(inp) > mylift.currFloor:
                print("lift moving up....")
                return mylift.moveUp(int(inp))
            elif int(inp) < mylift.currFloor:
                print("lift moving down....")
                return mylift.moveDown(int(inp))
            else:
                s ="Already on floor "+str(inp)+" enter some other floor"
                return s
        else:
            return "Enter some valid floor (0 to 3)"