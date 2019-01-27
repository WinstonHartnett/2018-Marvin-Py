import logging

from .chassis import Chassis
from .intake import Intake
from .lift import Lift
from .pneumatics import Pneumatics
from .winch import Winch

logger, i_chassis, i_intake, i_lift, i_winch, i_pneumatics = None, None, None, None, None, None


def init():
    global logger, i_chassis, i_intake, i_lift, i_winch, i_pneumatics

    logger = logging.getLogger("Subsystems")
    i_chassis = Chassis()
    i_intake = Intake()
    i_lift = Lift()
    i_winch = Winch()
    i_pneumatics = Pneumatics()
    logger.debug("Subsystems initialized")
