import commands
import logging

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

import subsystems
from inputs import oi


class Marvin(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        print("subs")
        oi.init()
        print("oi")
        commands.init()
        print("command")

        subsystems.chassis.setupEncoder()
        self.scheduler = Scheduler.getInstance()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        # subsystems.chassis.resetGyro()
        pass

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
