from .chassis import Chassis
from .lift import Lift
from .intake import Intake
from .winch import Winch


def init():
    global chassis, lift, intake, winch

    chassis = Chassis()
    lift = Lift()
    intake = Intake()
    winch = Winch()
