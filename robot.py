
import wpilib
from wpilib.drive import DifferentialDrive
controlDelDriver = {'B1':1,'B2':2,'B3':3,'B4':4,'B5':5,'B6':6}

class MyRobot(wpilib.SampleRobot):

    def robotInit(self):
        self.lstick = wpilib.Joystick(0)
        self.motor_DrivetrainDe = wpilib.VictorSP(1)
        self.motor_DrivetrainIz = wpilib.VictorSP(3)
        self.motor_CajadereduccionDe = wpilib.VictorSP(2)
        self.motor_CajadereduccionIz = wpilib.VictorSP(4)
        self.motor_Rodillos = wpilib.Spark(0)
        self.motor_RuedasLanzamiento = wpilib.Spark(5)
        self.motor_Enrolla = wpilib.Spark(6)
        self.G_motor = wpilib.SpeedControllerGroup(self.motor_CajadereduccionDe,self.motor_CajadereduccionIz)

        self.FinalCarreraGancho1 = wpilib.DigitalInput(0)
        self.FinalCarreraGancho2 = wpilib.DigitalInput(1)
        self.FinalCarreraTope = wpilib.DigitalInput(2)

    def disable(self):
        '''Called when the robot is disable'''
        while self.isDisabled():
            wpilib.Timer.delay(0.01)

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            wpilib.Timer.delay(0.01)

    def operatorControl(self):
        '''Called when operation control mode is enabled'''

        timer = wpilib.Timer()
        timer.start()
   

        while self.operatorControl() and self.isEnabled:
            if self.lstick.getRawButtonPressed(controlDelDriver['B2']):
                self.motor_Rodillos.set(1)
            else:
                self.motor_Rodillos.set(0)
        
            if self.lstick.getRawButtonPressed(controlDelDriver['B1']):
                self.motor_RuedasLanzamiento.set(1)
            else:
                self.motor_RuedasLanzamiento.set(0)
        
            if self.lstick.getRawButtonPressed(controlDelDriver['B5']):
                self.motor_Enrolla.set(1)
            else:
                self.motor_Enrolla.set(0)
        
            if self.lstick.getRawButtonPressed(controlDelDriver['B3']):
                self.G_motor.set(-0.7)
        
                if self.FinalCarreraTope.get()==True:
                    self.G_motor.set(0)

            if self.FinalCarreraGancho1.get()==True and self.FinalCarreraGancho2.get()==True:
                self.G_motor.set(-0.5)
            else:
                self.G_motor.set(0)
        

            wpilib.Timer.delay(0.02)
    
if __name__ == '__main__':
    wpilib.run(MyRobot)


     