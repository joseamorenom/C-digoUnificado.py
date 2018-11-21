import wpilib
from wpilib.drive import DifferentialDrive
controlDelDriver={“B1”:1,”B2”:2}

class MyRobot(wpilib.SampleRobot):
   '''Main robot class'''
  
 def robotInit(self):
    self.lstick = wpilib.Joystick
    self.motor_D1 = wpilib.VictorSP(3)
    self.motor_I1 = wpilib.VictorSP(4)
    self.motor_externo=wpilib.VictorSP(5)
    self.G_motor=SpeedControllerGroup(self.motor_D1, self.motor_I1)
       #motor_D1 y motor_D2 son los motores de la caja de reducción 	             
    self.finalCarrera1=wpilib.digitalInput(0)
    self.finalCarrera2=wpilib.digitalInput(1)
    self.finalCarreraTope=wpilib.digitalInput(2)

        
      
   def disabled(self):
       '''Called when the robot is disabled'''

   def autonomous(self):
       '''Called when autonomous mode is enabled'''
      
       while self.isAutonomous() and self.isEnabled():
           wpilib.Timer.delay(0.01)

   def operatorControl(self):
       '''Called when operation control mode is enabled'''

       while self.isOperatorControl() and self.isEnabled():

           # Move a motor with a Joystick
           self.motor.set(self.lstick.getY())

 	 while self.isOperatedControl() and self.isEnabled():

        if self.lstick.GetRawButtonPressed(controlDelDriver['B5']):
              self.motor_externo.set(1)         
        if self.lstick.GetRawButtonReleased(controlDelDriver['B5']):
              self.motor_externo.set(0)       

        if self.lstick.GetRawButtonPressed(controlDelDriver['B3']):
              self.G_motor.set(-0.7)
	        if self.FinalCarreraTope(1):
		          self.G_motor.set(0)
#Revisar si se pone así “(1)” que el final de carrera está activado

        if self.finalCarrera1.get(1) and self.finalCarrera2.get(1):
              self.G_motor.set(-0.5)
	      if self.lstick.GetRawButtonPressed(controlDelDriver['B6']:
		          self.G_motor.set(0)
		 
if __name__ == '__main__':
   wpilib.run(MyRobot)


