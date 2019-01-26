import commands
import logging

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

import subsystems
import inputs.oi as oi


class Marvin(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        oi.init()
        commands.init()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        subsystems.pneumatics.extend()

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        subsystems.pneumatics.retract()

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
