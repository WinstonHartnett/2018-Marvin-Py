import commands

import wpilib
from commandbased import CommandBasedRobot

import subsystems
from inputs import oi


class Marvin(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        oi.init()
        commands.init()

        subsystems.chassis.setupEncoder()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        subsystems.chassis.resetGyro()

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
