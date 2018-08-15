import wpilib
from commandbased import CommandBasedRobot

import subsystems
from inputs import oi


class Marvin(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        oi.init()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
