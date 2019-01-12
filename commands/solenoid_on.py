from wpilib.command import Command
import subsystems


class Solenoid_On(Command):

    def __init__(self):
        self.requires(subsystems.pneumatics)

    def execute(self):
        subsystems.pneumatics.turnOn()