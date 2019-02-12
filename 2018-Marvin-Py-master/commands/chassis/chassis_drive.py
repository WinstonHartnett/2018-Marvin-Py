from wpilib.command import Command

import subsystems


class Chassis_Drive(Command):

    def __init__(self):
        super().__init__("Chassis_Drive")
        self.requires(subsystems.i_chassis)

    def execute(self):
        subsystems.i_chassis.joystickDrive()

    def isFinished(self):
        return False
