from wpilib.command import Command

import constants
import sub as s


class DriveNormal(Command):

    def __init__(self): self.requires(s.sub_drive)

    def execute(self): s.sub_drive.joystickDrive()

    def isFinished(self): return False


class SetDriveSpeed(Command):

    def __init__(self, spd_new): self.spd = spd_new

    def execute(self): s.sub_drive.setDriveSpd(self.spd)

    def isFinished(self): return True


class SetRotateSpeed(Command):

    def __init__(self, spd_new): self.spd = spd_new

    def execute(self): s.sub_drive.setRotateSpd(self.spd)

    def isFinished(self): return True
