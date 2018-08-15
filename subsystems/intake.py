import time
from commands.boxintake import BoxIntake

from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup
from wpilib.command import Subsystem

import robotmap


class Intake(Subsystem):

    def __init__(self):
        self.talon_1 = WPI_TalonSRX(robotmap.talon_intake_1)
        self.talon_2 = WPI_TalonSRX(robotmap.talon_intake_2)
        self.talon_group = SpeedControllerGroup(self.talon_1, self.talon_2)

    def setSpd(self, spd_new):
        robotmap.spd_intake = spd_new

    # Fix this
    def intake(self, spd_temp=None, is_fixed=None):
        self.talon_1.setInverted(True)
        self.talon_2.setInverted(False)
        if spd_temp == None and is_fixed == None:
            pass                                        # TODO
        elif spd_temp != None and is_fixed == None:
            self.talon_group.set(spd_temp)
        elif spd_temp != None and is_fixed != None:
            self.talon_group.set(robotmap.spd_intake)
        else:
            raise("intake() fail!")

    def eject(self, spd_temp=None, is_fixed=None):
        self.talon_1.setInverted(False)
        self.talon_2.setInverted(True)
        if spd_temp == None and is_fixed == None:
            pass                                        # TODO
        elif spd_temp != None and is_fixed == None:
            self.talon_group.set(spd_temp)
        elif spd_temp != None and is_fixed != None:
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
        self.setDefaultCommand(BoxIntake())
