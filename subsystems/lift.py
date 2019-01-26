from ctre import WPI_TalonSRX
from wpilib.command import Subsystem

import robotmap


class Lift(Subsystem):

    def __init__(self):
        super().__init__("Lift")
        self.talon_lift = WPI_TalonSRX(robotmap.talon_lift)

    @classmethod
    def setSpd(cls, spd_new):
        robotmap.spd_lift = spd_new

    def raiseLift(self):
        self.talon_lift.setInverted(False)
        self.talon_lift.set(robotmap.spd_lift)

    def lowerLift(self):
        self.talon_lift.setInverted(True)
        self.talon_lift.set(robotmap.spd_lift_lower)

    def stop(self):
        self.talon_lift.stopMotor()
