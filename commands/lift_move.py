from wpilib.command import Command

import subsystems


class Lift_Move(Command):

    def __init__(self, direction=bool, speed=None):
        self.requires(subsystems.lift)
        self.direction = direction
        if speed is None:
            pass
        elif speed is not None:
            self.speed = speed

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
