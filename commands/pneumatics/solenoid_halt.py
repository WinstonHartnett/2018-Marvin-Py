from wpilib.command import InstantCommand

import subsystems

class SolenoidHalt(InstantCommand):

    def __init__(self):
        super().__init__('SolenoidHalt')
        self.requires(subsystems._pneumatics)

    def execute(self):
        subsystems._pneumatics.halt()