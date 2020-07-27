"""create a class CRobot who generate a robot defined by:
- features: type, sn, orientation, state(on,off,maintenance)
- methodes:
*constructeur robot () or robot(type,sn)
*getType() : returns the type of robot
*getSN(): returns the sn of the robot
*getOrientation()
*getState()
*turn(): turn the robot of 1/4 tour
*display(): show robot informations

-the direction is an attribut of integer type 1,2,3 or 4 (N,E,S,OE)
-turn makes a rotation on the left to the robot
-display allows to show all the infos of the robot"""

class CRobot (object):

    def __init__(self, type, sn, orientation=1, state=False):
        self.type=type
        self.sn=sn
        self.orientation=orientation
        self.state=state

    def getType(self):
        return self.type

    def getSN(self):
        return self.sn

    def getOrientation(self):
        return self.orientation

    def getState(self):
        return self.state

    def setOrientation(self,new_orientation):
        self.orientation=new_orientation

    def setState(self, new_state):
        if self.state is True:
            print("Robot is already ON")
        else:
            while new_state is not True or False:
                print("Possible values are: True or False")
            self.state=new_state

    def turnRobot(self):
        if self.orientation==1:
            self.orientation=4
        else:
            self.orientation-=1

    def displayRobot(self):
        print("type: {}, sn: {}, orientation: {}, state: {}".format(self.type,self.sn,self.orientation,self.state))

class CRobotMobile (CRobot):
    #def __init__(self):

    def __init__(self, type, sn, x_init=0, y_init=0):
        CRobot.__init__(self,type,sn)
        self.x=x_init
        self.y=y_init

    def displayPosition(self):
        print("X: ", self.x)
        print("Y: ", self.y, "\n")

    def displayRobotMobile(self):
        self.displayRobot()
        self.displayPosition()

    def moveRobotMobile(self, step):
        if self.state is False:
            print("The robot is turned OFF")
        else:
            #North
            if self.orientation==1:
                self.y+=step
            #East
            if self.orientation == 2:
                self.x+=step

            #South
            if self.orientation == 3:
                self.y-=step

            #West
            if self.orientation == 4:
                self.x -= step
