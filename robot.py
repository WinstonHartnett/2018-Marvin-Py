import wpilib
from commandbased import CommandBasedRobot

import oi
import sub


class Marvin(CommandBasedRobot):

    def robotInit(self):
        sub.init()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
