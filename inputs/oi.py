from wpilib import Joystick

import robotmap


def init():
    global joystick

    joystick = Joystick(robotmap.joystick)
