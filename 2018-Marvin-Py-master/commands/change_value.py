from wpilib.command import Command


class Change_Value(Command):

    def __init__(self, key, value):
        self.key = key              # e.g. robotmap.spd_chassis_drive
        self.value = value          # e.g. 0.4

    def initialize(self):
        self.key = self.value

    def isFinished(self):
        return True
