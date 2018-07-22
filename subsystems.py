import time

from ctre import ControlMode, WPI_TalonSRX
from wpilib import (ADXRS450_Gyro, DigitalInput, Encoder, PIDController,
                    SpeedControllerGroup)
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive
from wpilib.spark import Spark

import constants
import oi


class Sub_Drive(Subsystem):

    spd_cont_L1 = Spark(constants.spark_front_left)
    spd_cont_R1 = Spark(constants.spark_front_right)
    spd_cont_L2 = Spark(constants.spark_back_left)
    spd_cont_R2 = Spark(constants.spark_back_right)

    spd_cont_grp_L = SpeedControllerGroup(spd_cont_L1, spd_cont_L2)
    spd_cont_grp_R = SpeedControllerGroup(spd_cont_R1, spd_cont_R2)
    spd_cont_grp_C = SpeedControllerGroup(
        spd_cont_L1, spd_cont_L2, spd_cont_R1, spd_cont_R2)

    drive = DifferentialDrive(spd_cont_grp_L, spd_cont_grp_R)
    gyro = ADXRS450_Gyro(1)

    encoder_L = Encoder(constants.encoder_left_1, constants.encoder_left_2)
    encoder_R = Encoder(constants.encoder_right_1, constants.encoder_right_2)

    p = 0.015
    pid_cont = PIDController(p, 0, 0, encoder_L, spd_cont_grp_C)

    def setupEncoder(self):
        # self.encoder_L.setDistancePerPulse(constants.distance_per_pulse)
        # self.encoder_R.setDistancePerPulse(constants.distance_per_pulse)
        self.pid_cont.setAbsoluteTolerance(5)
        self.pid_cont.setOutputRange(-0.6, 0.6)
        # self.encoder_L.reset()
        # self.encoder_R.reset()

    def setDriveSpd(self, spd_drive_new):
        constants.spd_drive = spd_drive_new

    def setRotateSpd(self, spd_rotate_new):
        constants.spd_rotate = spd_rotate_new

    def curveDrive(self, xSpeed, zRotation):
        self.drive.curvatureDrive(xSpeed, zRotation, True)

    def joystickDrive(self):
        self.drive.curvatureDrive(-oi.getJoystick().getAxis(1) * constants.spd_drive,
                                  oi.getJoystick().getAxis(4) * constants.spd_rotate, True)

    def stop(self):
        self.drive.stopMotor()

    def getGyroAngle(self):
        return self.gyro.getAngle()

    def resetGyro(self):
        self.gyro.reset()

    def gyroDrive(self, spd_temp, amt_turn=None):
        if amt_turn is None:
            self.curveDrive(spd_temp, 0.0)
        else:
            self.curveDrive(spd_temp, amt_turn)

    def initDefaultCommand(self):
        pass


class Sub_Intake(Subsystem):

    spd_cont_1 = WPI_TalonSRX(1)
    spd_cont_2 = WPI_TalonSRX(2)
    spd_cont_grp = SpeedControllerGroup(spd_cont_1, spd_cont_2)

    def setSpeed(self, spd_intake_new):
        constants.spd_intake = spd_intake_new

    def boxIntake(self, spd_intake_new=None, is_Fixed=None):
        self.spd_cont_1.setInverted(True)
        self.spd_cont_2.setInverted(False)

        if spd_intake_new == None & is_Fixed == None:
            if oi.getJoystick().getAxis(2) - oi.getJoystick().getAxis(3) >= 0.8:
                self.spd_cont_grp.set(constants.spd_intake)
            else:
                self.spd_cont_grp.set(oi.getJoystick().getAxis(
                    2) - oi.getJoystick().getAxis(3))
        elif spd_intake_new != None:
            self.setSpeed(spd_intake_new)
            self.spd_cont_grp.set(constants.spd_intake)
        elif is_Fixed != None:
            self.spd_cont_grp.set(constants.spd_intake)

    def boxEject(self, spd_intake_new=None, is_Fixed=None):
        self.spd_cont_1.setInverted(False)
        self.spd_cont_2.setInverted(True)

        if spd_intake_new == None & is_Fixed == None:
            self.spd_cont_grp.set(oi.getJoystick().getAxis(3))
        elif spd_intake_new != None:
            self.setSpeed(spd_intake_new)
            self.spd_cont_grp.set(constants.spd_intake)
        elif is_Fixed != None:
            self.spd_cont_grp.set(constants.spd_intake)

    def boxDislodge(self):
        self.boxEject(True)
        time.sleep(0.1)
        self.boxIntake(True)
        time.sleep(0.2)

    def boxStop(self):
        self.spd_cont_grp.set(0.0)

    def initDefaultCommand(self):
        pass


class Sub_Lift(Subsystem):

    lim_top = DigitalInput(9)
    lim_bot = DigitalInput(8)

    spd_cont_lift = WPI_TalonSRX(3)

    def setSpeed(self, spd_lift_new):
        constants.spd_lift = spd_lift_new

    def raiseLift(self):
        self.spd_cont_lift.setInverted(False)
        self.spd_cont_lift.set(ControlMode.PercentOutput, constants.spd_lift)

    def lowerLift(self):
        self.spd_cont_lift.setInverted(True)
        self.spd_cont_lift.set(ControlMode.PercentOutput,
                               constants.spd_lift_lower)

    def holdLift(self):
        self.spd_cont_lift.set(ControlMode.PercentOutput, 0.0)
        time.sleep(0.03)
        self.spd_cont_lift.set(ControlMode.PercentOutput, 0.4)
        time.sleep(0.04)

    def stopLift(self):
        self.spd_cont_lift.set(ControlMode.PercentOutput, 0.0)

    def initDefaultCommand(self):
        pass


class Sub_Taster(Subsystem):

    spd_cont_taster = WPI_TalonSRX(4)

    def setSpeed(self, spd_taster_new):
        constants.spd_taster = spd_taster_new

    def raiseTaster(self):
        self.spd_cont_taster.set(
            ControlMode.PercentOutput, constants.spd_taster)

    def lowerTaster(self):
        self.spd_cont_taster.set(
            ControlMode.PercentOutput, -constants.spd_taster)

    def stop(self):
        self.spd_cont_taster.set(ControlMode.PercentOutput, 0.0)

    def initDefaultCommand(self):
        pass


class Sub_Winch(Subsystem):

    spd_cont_winch = Spark(5)

    def setSpeed(self, spd_winch_new):
        constants.spd_winch = spd_winch_new

    def raiseWinch(self):
        self.spd_cont_winch.setInverted(True)
        self.spd_cont_winch.set(constants.spd_winch)

    def stopWinch(self):
        self.spd_cont_winch.set(0.0)

    def initDefaultCommand(self):
        pass
