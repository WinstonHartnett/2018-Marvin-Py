import logging

import oi
import robotmap

from .chassis.chassis_drive import Chassis_Drive

logger = None


def init():
    global logger
    logger = logging.getLogger("Commands")
    oi.start.whenPressed(Chassis_Drive())
    logger.debug("Commands initialized")
