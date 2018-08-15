from wpilib.command import Command

import subsystems


class BoxIntake(Command):

    def __init__(self):
        self.requires(subsystems.intake)

    def execute(self):
        subsystems.intake.intake()

    def isFinished(self):
        return False

    def end(self):
        subsystems.intake.stop()

    def interrupted(self):
        self.end()
