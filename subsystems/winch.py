from wpilib import Spark
from wpilib.command import Subsystem

import robotmap


class Winch(Subsystem):

    def __init__(self):
        self.spark_winch = Spark(robotmap.spark_winch)

    def setSpd(self, spd_new):
        robotmap.spd_winch = spd_new

    def raiseWinch(self):
        self.spark_winch.setInverted(True)
        self.spark_winch.set(robotmap.spd_winch)

    def stopWinch(self):
        self.spark_winch.set(0.0)

    def initDefaultCommand(self):
        pass
