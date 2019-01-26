import time

from wpilib import Solenoid
from wpilib.command import Subsystem

import robotmap


class Pneumatics(Subsystem):

    def __init__(self):
        self.solenoid_R = Solenoid(robotmap.solenoid_R)
        self.solenoid_L = Solenoid(robotmap.solenoid_L)
        self.is_active = False

    def extend(self):
        self.solenoid_L.set(False)
        self.solenoid_R.set(True)

    def retract(self):
        self.solenoid_R.set(False)
        self.solenoid_L.set(True)

    def halt(self):
        self.solenoid_R.set(False)
        self.solenoid_L.set(False)

    def get_active(self):
        return self.is_active

    def alternate(self):
        pass
