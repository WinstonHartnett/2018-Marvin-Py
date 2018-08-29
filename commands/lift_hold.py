from wpilib.command import Command

import subsystems


class Lift_Hold(Command):

    def __init__(self):
        self.requires(subsystems.lift)

    def execute(self):
        pass                # TODO Add limit switches

    def isFinished(self):
        return False

    def end(self):
        subsystems.lift.stop()

    def interrupted(self):
        self.end()
