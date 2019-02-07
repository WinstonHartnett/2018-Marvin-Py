from wpilib.command import InstantCommand
from wpilib import Timer
import subsystems

class SolenoidRetract(InstantCommand):

    def __init__(self):
        super().__init__('SolenoidRetract')
        self.requires(subsystems._pneumatics)

    def execute(self):
        if subsystems._pneumatics.solenoid_L.get() and not subsystems._pneumatics.solenoid_R.get():
            pass
        else:
            subsystems._pneumatics.retract()