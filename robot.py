import commands
import logging

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

import inputs.oi
import subsystems


class Marvin(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        inputs.oi.init()
        commands.init()
        print(type(inputs.oi.A))

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        Scheduler().getInstance().run()
        print(subsystems._pneumatics.solenoid_L.get())
        print(subsystems._pneumatics.solenoid_R.get())

    def testPeriodic(self):
        pass

if __name__ == '__main__':
    wpilib.run(Marvin)
