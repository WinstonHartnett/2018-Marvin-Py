from .chassis import Chassis
from .intake import Intake
from .lift import Lift
from .pneumatics import Pneumatics
from .winch import Winch

_chassis, _intake, _lift, _winch, _pneumatics = None, None, None, None, None


def init():
    global _chassis, _intake, _lift, _winch, _pneumatics

    _chassis = Chassis()
    _intake = Intake()
    _lift = Lift()
    _winch = Winch()
    _pneumatics = Pneumatics()
