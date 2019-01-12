from .chassis import Chassis
from .intake import Intake
from .lift import Lift
from .winch import Winch
from .pneumatics import Pneumatics

chassis, intake, lift, winch, pneumatics = None, None, None, None, None


def init():
    global chassis, intake, lift, winch, pneumatics

    chassis = Chassis()
    intake = Intake()
    lift = Lift()
    winch = Winch()
    pneumatics = Pneumatics()
