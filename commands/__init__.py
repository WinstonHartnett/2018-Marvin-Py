from inputs import oi
from .chassis_drive import Chassis_Drive


def init():
    oi.A.whenPressed(Chassis_Drive)
