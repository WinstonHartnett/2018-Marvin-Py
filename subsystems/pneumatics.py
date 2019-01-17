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
        if self.is_active is False:
            self.time = time.time()
            self.time -= self.time
            self.is_active = True
        elif self.is_active:
            pass

        if ((time.time() - self.time()) <= (robotmap.pneumatics_alternate_period / 2)):
            self.extend()
        elif ((time.time() - self.time()) >= (robotmap.pneumatics_alternate_period / 2)) and ((time.time() - self.time()) <= robotmap.pneumatics_alternate_period):
            self.retract()
        else:
            self.halt()
            self.is_active = False
