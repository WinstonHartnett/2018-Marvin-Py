from .chassis import Chassis
from .intake import Intake
from .lift import Lift
from .winch import Winch

chassis, intake, lift, winch = None, None, None, None


def init():
    global chassis, intake, lift, winch

    chassis = Chassis()
    intake = Intake()
    lift = Lift()
    winch = Winch()
