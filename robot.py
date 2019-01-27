import commands
import logging

import wpilib
from commandbased import CommandBasedRobot

import oi
import subsystems


class Marvin(CommandBasedRobot):

    def robotInit(self):
        self.logger = logging.getLogger("Core")
        subsystems.init()
        oi.init()
        commands.init()
        self.logger.warning("Robot initialized")

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
