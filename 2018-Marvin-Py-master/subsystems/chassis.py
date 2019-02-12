import commands
from math import pi

from wpilib import ADXRS450_Gyro, Encoder, Spark, SpeedControllerGroup
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive

import robotmap
from inputs import oi


class Chassis(Subsystem):

    def __init__(self):
        super().__init__("Chassis")
        self.spark_L1 = Spark(robotmap.spark_L1)
        self.spark_L2 = Spark(robotmap.spark_L2)
        self.spark_R1 = Spark(robotmap.spark_R1)
        self.spark_R2 = Spark(robotmap.spark_R2)
        self.spark_group_L = SpeedControllerGroup(self.spark_L1, self.spark_L2)
        self.spark_group_R = SpeedControllerGroup(self.spark_R1, self.spark_R2)
        self.drive = DifferentialDrive(self.spark_group_L, self.spark_group_R)

        self.gyro = ADXRS450_Gyro(robotmap.gyro)

        self.encoder_L = Encoder(0, 1)
        self.encoder_R = Encoder(2, 3)

        self.dist_pulse_L = pi * 6 / 2048
        self.dist_pulse_R = pi * 6 / 425

    @classmethod
    def setDriveSpd(cls, spd_drive_new):
        robotmap.spd_chassis_drive = spd_drive_new

    @classmethod
    def setRotateSpd(cls, spd_rotate_new):
        robotmap.spd_chassis_rotate = spd_rotate_new

    def stop(self):
        self.drive.stopMotor()

    def curvatureDrive(self, spd_x, spd_z):
        self.drive.curvatureDrive(spd_x, spd_z, True)

    def joystickDrive(self):
        self.drive.curvatureDrive(-(oi.joystick.getRawAxis(1))
                                  * robotmap.spd_chassis_drive, oi.joystick.getRawAxis(4) * robotmap.spd_chassis_rotate, True)

    def setupEncoder(self):
        self.encoder_L.setDistancePerPulse(self.dist_pulse_L)
        self.encoder_R.setDistancePerPulse(self.dist_pulse_R)
        self.encoder_L.reset()
        self.encoder_R.reset()

    def getGyroAngle(self):
        return self.gyro.getAngle()

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
        from commands.chassis_drive import Chassis_Drive
        self.setDefaultCommand(Chassis_Drive())
