from wpilib.command import Command
import subsystems


class JoystickDrive(Command):

    def __init__(self):
        self.requires(subsystems.chassis)

    def execute(self):
        subsystems.chassis.joystickDrive()

    def isFinished(self):
        return False
