import inputs.oi as oi
import robotmap

from .chassis_drive import Chassis_Drive


def init():
    oi.start.whenPressed(Chassis_Drive())
