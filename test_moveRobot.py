import CRobot

#creating robot C14 type_1
C14=CRobot.CRobotMobile("type_1", "121126072020")

#turning the robot to East
C14.setOrientation(2)
C14.setState(True)
C14.displayRobotMobile()

#moving robot to 4 towards West
C14.setOrientation(4)
C14.moveRobotMobile(4)
C14.displayPosition()

#moving robot to 6 towards North
C14.setOrientation(1)
C14.moveRobotMobile(6)
C14.displayPosition()

#moving robot to 14 towards East
C14.setOrientation(2)
C14.moveRobotMobile(14)
C14.displayPosition()

#step back robot to 5 towards South
C14.setOrientation(1)
C14.moveRobotMobile(8)
C14.displayPosition()

