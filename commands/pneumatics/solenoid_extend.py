from wpilib.command import InstantCommand

import subsystems

class SolenoidExtend(InstantCommand):

    def __init__(self):
        super().__init__('SolenoidExtend')
        self.requires(subsystems._pneumatics)

    def execute(self):
        subsystems._pneumatics.extend()