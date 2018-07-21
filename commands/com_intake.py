import wpilib.command

import constants
import sub as s

class DislodgeBox(wpilib.command.Command):

    def __init__(self): self.requires(s.sub_intake)

    def execute(self): s.sub_intake.boxDislodge()

    def isFinished(self): return False

    def end(self): s.sub_intake.boxStop()

    def interrupted(self): self.end()


class IntakeBox(wpilib.command.Command):

    def __init__(self): self.requires(s.sub_intake)

    def execute(self): s.sub_intake.boxIntake()

    def isFinished(self): return False

    def end(self): s.sub_intake.boxStop()

    def interrupted(self): self.end()


class EjectBox(wpilib.command.Command):

    def __init__(self): self.requires(s.sub_intake)

    def execute(self): s.sub_intake.boxEject()

    def isFinished(self): return False

    def end(self): s.sub_intake.boxStop()

    def interrupted(self): self.end()
