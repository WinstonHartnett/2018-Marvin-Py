from wpilib.command import Command


class ChangeValue(Command):

    def __init__(self, value, number):
        self.value = value
        self.number = number

    def initialize(self):
        self.value = self.number

    def isFinished(self):
        return True
