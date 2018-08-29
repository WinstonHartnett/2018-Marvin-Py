from wpilib import Spark
from wpilib.command import Subsystem

import robotmap


class Winch(Subsystem):

    def __init__(self):
        self.spark_winch = Spark(robotmap.spark_winch)

    @classmethod
    def setSpd(cls, spd_new):
        robotmap.spd_winch = spd_new

    def raiseWinch(self):
        self.spark_winch.setInverted(True)
        self.spark_winch.set(robotmap.spd_winch)

    def stop(self):
        self.spark_winch.set(0.0)

    def initDefaultCommand(self):
        pass
