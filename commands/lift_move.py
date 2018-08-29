from wpilib.command import Command

import subsystems


class Lift_Move(Command):

    def __init__(self, direction):
        self.requires(subsystems.lift)
        self.direction = direction

    def execute(self):
        if self.direction is True:
            pass                        # TODO Limit switches
        elif self.direction is False:
            pass                        # TODO Limit switches
        else:
            self.end()

    def isFinished(self):
        return False

    def end(self):
        subsystems.lift.stop()
