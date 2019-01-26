import commands
import logging

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

import inputs.oi as oi
import subsystems


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
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        from commands.chassis_drive import Chassis_Drive
        Chassis_Drive().start()

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
