import wpilib.command

import constants
import sub as s


class LowerTaster(wpilib.command.Command):

    def __init__(self): self.requires(s.sub_taster)

    def execute(self): s.sub_taster.lowerTaster()

    def end(self): s.sub_taster.stop()

    def interrupted(self): self.end()


class RaiseTaster(wpilib.command.Command):

    def __init__(self): self.requires(s.sub_taster)

    def execute(self): s.sub_taster.raiseTaster()

    def isFinished(self): False

    def end(self): s.sub_taster.stop()

    def interrupted(self): self.end()


class SetTasterSpeed(wpilib.command.Command):

    def __init__(self, spd_new): self.spd = spd_new

    def execute(self): s.sub_taster.setSpeed(self.spd)

    def isFinished(self): False

    def end(self): s.sub_taster.stop()

    def interrupted(self): self.end()
