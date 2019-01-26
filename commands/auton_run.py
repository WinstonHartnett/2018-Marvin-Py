import logging

from wpilib import DriverStation
from wpilib.command import Command

import robotmap


class Auton_Run(Command):

    def __init__(self):
        self.logger = logging.getLogger("Marvin")

    def reportCase(self, loc_switch, auton_location=int):
        self.logger.info("Auton case is: " + loc_switch + auton_location)

    def initialize(self):
        loc_switch = DriverStation.getInstance().getGameSpecificMessage()[0]
        loc_scale = DriverStation.getInstance().getGameSpecificMessage()[1]

        # TODO Add command chains
        if robotmap.auton_target == 0:
            if loc_switch == 'L':
                if robotmap.auton_location == 1:
                    self.reportCase(loc_switch, robotmap.auton_location)
                elif robotmap.auton_location == 2:
                    self.reportCase(loc_switch, robotmap.auton_location)
                elif robotmap.auton_location == 3:
                    self.reportCase(loc_switch, robotmap.auton_location)
                else:
                    self.logger.error("Auton failed to start!")
            elif loc_switch == 'R':
                if robotmap.auton_location == 1:
                    self.reportCase(loc_switch, robotmap.auton_location)
                elif robotmap.auton_location == 2:
                    self.reportCase(loc_switch, robotmap.auton_location)
                elif robotmap.auton_location == 3:
                    self.reportCase(loc_switch, robotmap.auton_location)
                else:
                    self.logger.error("Auton failed to start!")
            else:
                self.logger.error("Auton failed to start!")
        elif robotmap.auton_target == 1:
            if loc_scale == 'L':
                if robotmap.auton_location == 1:
                    self.reportCase(loc_scale, robotmap.auton_location)
                elif robotmap.auton_location == 3:
                    self.reportCase(loc_scale, robotmap.auton_location)
            elif loc_scale == 'R':
                if robotmap.auton_location == 1:
                    self.reportCase(loc_scale, robotmap.auton_location)
                elif robotmap.auton_location == 3:
                    self.reportCase(loc_scale, robotmap.auton_location)
            else:
                self.logger.error("Auton failed to start!")

    def execute(self):
        pass

    def isFinished(self):
        return False

    def end(self):
        pass

    def interrupted(self):
        pass
