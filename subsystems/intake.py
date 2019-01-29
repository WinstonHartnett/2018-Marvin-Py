import time

from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup
from wpilib.command import Subsystem

import robotmap
import inputs.oi as oi


class Intake(Subsystem):

    def __init__(self):
        super().__init__("Intake")
        self.talon_1 = WPI_TalonSRX(robotmap.talon_intake_1)
        self.talon_2 = WPI_TalonSRX(robotmap.talon_intake_2)
        self.talon_group = SpeedControllerGroup(self.talon_1, self.talon_2)

    @classmethod
    def setSpd(cls, spd_new):
        robotmap.spd_intake = spd_new

    def intake(self, spd_temp=None, is_fixed=None):
        self.talon_1.setInverted(True)
        self.talon_2.setInverted(False)
        if (spd_temp is None) and (is_fixed is None):
            if oi.joystick.getAxis(2) - oi.joystick.getAxis(3) >= 0.8:
                self.talon_group.set(0.8)
            elif oi.joystick.getAxis(2) - oi.joystick.getAxis(3) < 0.8:
                self.talon_group.set(oi.joystick.getAxis(
                    2) - oi.joystick.getAxis(3))
        elif (spd_temp is not None) and (is_fixed is None):
            self.talon_group.set(spd_temp)
        elif (spd_temp is not None) and (is_fixed is not None):
            self.talon_group.set(robotmap.spd_intake)
        else:
            raise("intake() fail!")

    def eject(self, spd_temp=None, is_fixed=None):
        self.talon_1.setInverted(False)
        self.talon_2.setInverted(True)
        if (spd_temp is None) and (is_fixed is None):
            self.talon_group.set(oi.joystick.getAxis(3))
        elif (spd_temp is not None) and (is_fixed is None):
            self.talon_group.set(spd_temp)
        elif (spd_temp is not None) and (is_fixed is not None):
            self.talon_group.set(robotmap.spd_intake)
        else:
            raise("eject() fail!")

    def dislodge(self):
        self.eject(True)
        time.sleep(0.1)
        self.intake(True)
        time.sleep(0.2)

    def stop(self):
        self.talon_group.stopMotor()

    def initDefaultCommand(self):
        pass
