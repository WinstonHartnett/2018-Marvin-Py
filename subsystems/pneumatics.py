from wpilib import Solenoid
from wpilib.command import Subsystem


class Pneumatics(Subsystem):

    def __init__(self):
        self.solenoid = Solenoid(3)

    def turnOn(self):
        # self.solenoid.setPulseDuration()
        self.solenoid.startPulse()
