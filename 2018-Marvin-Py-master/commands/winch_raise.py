from wpilib.command import Command

import subsystems


class Winch_Raise(Command):

    def __init__(self):
        self.requires(subsystems.winch)

    def execute(self):
        subsystems.winch.raiseWinch()

    def isFinished(self):
        return False

    def end(self):
        subsystems.winch.stop()
