from wpilib.command import InstantCommand

import subsystems


class Solenoid_Move(InstantCommand):

    def __init__(self):
        self.requires(subsystems.pneumatics)

    def execute(self):
        if subsystems.pneumatics.solenoid_L.get():
            subsystems.pneumatics.extend()
        elif subsystems.pneumatics.solenoid_R.get():
            subsystems.pneumatics.retract()
        elif subsystems.pneumatics.solenoid_L.get() and subsystems.pneumatics.solenoid_R.get():
            pass
        else:
            pass
