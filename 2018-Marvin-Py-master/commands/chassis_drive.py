from wpilib.command import Command

import subsystems


class Chassis_Drive(Command):

    def __init__(self):
        super().__init__("Chassis_Drive")
        self.requires(subsystems._chassis)

    def execute(self):
        subsystems._chassis.joystickDrive()

    def isFinished(self):
        return False
