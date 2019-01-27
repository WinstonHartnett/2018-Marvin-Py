from wpilib.command import Command

import subsystems


class Solenoid_Alternate(Command):

    def __init__(self):
        self.requires(subsystems.pneumatics)

    def initialize(self):
        pass

    def execute(self):
        pass

    def isFinished(self):
        pass

    def interrupted(self):
        pass

    def end(self):
        pass
