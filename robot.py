
import commands

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

import subsystems
from inputs import oi


class Marvin(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        oi.init()
        commands.init()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        subsystems.chassis.resetGyro()

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
