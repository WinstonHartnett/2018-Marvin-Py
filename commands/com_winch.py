import wpilib.command

import constants
import sub as s


class RaiseWinch(wpilib.command.Command):

    def __init__(self): self.requires(s.sub_winch)

    def execute(self): s.sub_winch.raiseWinch()

    def isFinished(self): return False

    def end(self): s.sub_winch.stopWinch()

    def interrupted(self): self.end()


class StopWinch(wpilib.command.Command):

    def __init__(self): self.requires(s.sub_winch)

    def execute(self):s.sub_winch.stopWinch()

    def isFinished(self): return False

    def end(self): s.sub_winch.stopWinch()

    def interrupted(self): self.end()


class SetWinchSpeed(wpilib.command.Command):

    def __init__(self, spd_new): self.spd = spd_new

    def execute(self): s.sub_winch.setSpeed(self.spd)

    def isFinished(self): return True
