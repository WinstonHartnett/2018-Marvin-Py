import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

import oi
import sub
from dashboard import Dashboard


class Marvin(CommandBasedRobot):

    def robotInit(self):
        sub.init()

        self.dashboard = Dashboard()
        self.dashboard.init()

    def disabledInit(self):
        Scheduler.getInstance().removeAll()

    def disabledPeriodic(self):
        Scheduler.getInstance().run()

    def teleopInit(self):
        sub.sub_drive.setupEncoder()
        sub.sub_drive.resetGyro()
        sub.sub_drive.spd_cont_L1.setInverted(False)
        sub.sub_drive.spd_cont_L2.setInverted(False)

    def teleopPeriodic(self):
        self.dashboard.poll()
        self.dashboard.start()
        Scheduler.getInstance().run()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
