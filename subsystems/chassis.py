from commands.joystickdrive import JoystickDrive

from wpilib import ADXRS450_Gyro, Spark, SpeedControllerGroup
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive

import robotmap
from inputs import xboxcontroller


class Chassis(Subsystem):

    def __init__(self):
        self.spark_L1 = Spark(robotmap.spark_L1)
        self.spark_L2 = Spark(robotmap.spark_L2)
        self.spark_R1 = Spark(robotmap.spark_R1)
        self.spark_R2 = Spark(robotmap.spark_R2)
        self.spark_group_L = SpeedControllerGroup(self.spark_L1, self.spark_L2)
        self.spark_group_R = SpeedControllerGroup(self.spark_R1, self.spark_R2)
        self.drive = DifferentialDrive(self.spark_group_L, self.spark_group_R)
        self.gyro = ADXRS450_Gyro()

    def setDriveSpd(self, spd_drive_new):
        robotmap.spd_chassis_drive = spd_drive_new

    def setRotateSpd(self, spd_rotate_new):
        robotmap.spd_chassis_rotate = spd_rotate_new

    def stop(self): self.drive.stopMotor()

    def curvatureDrive(self, spd_x, spd_z):
        self.drive.curvatureDrive(spd_x, spd_z, True)

    def joystickDrive(self):
        self.drive.curvatureDrive(-(xboxcontroller.joystick.getRawAxis(1))
                                  * robotmap.spd_chassis_drive, xboxcontroller.joystick.getRawAxis(4) * robotmap.spd_chassis_rotate, True)

    def getGyroAngle(self, parameter_list):
        pass            # TODO

    def resetGyro(self):
        self.gyro.reset()

    def gyroDrive(self, spd_temp, amt_turn=None):
        if spd_temp and amt_turn is not None:
            self.curvatureDrive(spd_temp, amt_turn)
        elif amt_turn is None:
            self.curvatureDrive(spd_temp, 0.0)
        else:
            raise("GyroDrive() failed!")

    def initDefaultCommand(self):
        self.setDefaultCommand(JoystickDrive())
