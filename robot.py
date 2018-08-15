
import wpilib
from commandbased import CommandBasedRobot

import subsystems
from inputs import xboxcontroller


class Marvin(CommandBasedRobot):

    def robotInit(self):
        xboxcontroller.init()
        subsystems.init()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        subsystems.chassis.joystickDrive()

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
