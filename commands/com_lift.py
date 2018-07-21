import wpilib.command

import constants
import sub as s


class RaiseLift(wpilib.command.Command):

    def __init__(self):
        self.requires(s.sub_lift)

    def execute(self):
        if s.sub_lift.lim_top.get():
            s.sub_lift.raiseLift()
        elif not s.sub_lift.lim_top.get():
            s.sub_lift.holdLift()
        else:
            s.sub_lift.stopLift()

    def isFinished(self):
        return False

    def end(self):
        s.sub_lift.stopLift()


class LowerLift(wpilib.command.Command):

    def __init__(self):
        self.requires(s.sub_lift)

    def execute(self):
        if s.sub_lift.lim_bot.get():
            s.sub_lift.lowerLift()
        else:
            s.sub_lift.stopLift()
    
    def end(self):
        s.sub_lift.stopLift()

    def interrupted(self):
        self.end()


class HoldLift(wpilib.command.Command):

    def __init__(self):
        self.requires(s.sub_lift)

    def execute(self):
        if s.sub_lift.lim_top.get():
            s.sub_lift.holdLift()
        else:
            s.sub_lift.stopLift()

    def end(self):
        s.sub_lift.stopLift()

    def interrupted(self):
        self.end()


class SetLiftSpeed(wpilib.command.Command):

    def __init__(self, spd_new):
        self.requires(s.sub_lift)
        self.spd = spd_new

    def execute(self):
        s.sub_lift.setSpeed(self.spd)

    def isFinished(self):
        return True
