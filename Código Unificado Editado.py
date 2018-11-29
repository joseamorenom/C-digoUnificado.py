
import wpilib
import wpilib.buttons
from wpilib.drive import DifferentialDrive
controlDelDriver = {'B1':1,'B2':2,'B3':3,'B4':4,'B5':5,'B6':6}

class MyRobot(wpilib.SampleRobot):

    def robotInit(self):
        self.lstick = wpilib.Joystick(0)
        self.motor_Rodillos = wpilib.Spark(0)
        self.motor_DrivetrainDe = wpilib.VictorSP(1)
        self.motor_DrivetrainIz = wpilib.VictorSP(2)
        self.motor_CajadereduccionDe = wpilib.VictorSP(3)
        self.motor_CajadereduccionIz = wpilib.VictorSP(4)
        self.motor_RuedasLanzamiento = wpilib.Spark(5)
        self.motor_Enrolla = wpilib.Spark(6)
        self.FinalCarreraGancho1 = wpilib.DigitalInput(0)
        self.FinalCarreraGancho2 = wpilib.DigitalInput(1)
        self.FinalCarreraTope = wpilib.DigitalInput(2)
        self.Kevin = wpilib.drive.DifferentialDrive(self.motor_DrivetrainIz,self.motor_DrivetrainDe)

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
   

        while self.operatorControl() and self.isEnabled():
            self.Kevin.arcadeDrive(self.lstick.getX(),self.lstick.getY()*-1)
            if self.lstick.getRawButton(controlDelDriver['B1'])==True:
                self.motor_RuedasLanzamiento.set(1)
            else:
                self.motor_RuedasLanzamiento.set(0)
            if self.lstick.getRawButton(controlDelDriver['B2'])==True:
                self.motor_Rodillos.set(1)
            else:
                self.motor_Rodillos.set(0)
            if self.lstick.getRawButton(controlDelDriver['B3'])==True and (self.FinalCarreraGancho1.get()==True or self.FinalCarreraGancho2.get()==True):
                self.motor_CajadereduccionIz.set(-1)
                self.motor_CajadereduccionDe.set(1)
            else:
               self.motor_CajadereduccionIz.set(0)
               self.motor_CajadereduccionDe.set(0) 
            #Hay que determinar como operar con los sensores de los ganchos.
            if self.lstick.getRawButton(controlDelDriver['B5'])==True and self.FinalCarreraTope.get()==False:
                self.motor_Enrolla.set(1)
            else:
                self.motor_Enrolla.set(0)
           
            wpilib.Timer.delay(0.02)
    
if __name__ == '__main__':
    wpilib.run(MyRobot)


     