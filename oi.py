from wpilib import Joystick
from wpilib.buttons import JoystickButton
from wpilib.command import Command
from commands.com_drive import DriveNormal, SetDriveSpeed, SetRotateSpeed
from commands.com_intake import DislodgeBox, EjectBox, IntakeBox
from commands.com_lift import HoldLift, LowerLift, RaiseLift
from commands.com_taster import LowerTaster, RaiseTaster, SetTasterSpeed
from commands.com_winch import RaiseWinch, SetWinchSpeed, StopWinch


joystick = button_A = button_X = button_Y = trigger_L = trigger_R = bumper_L = bumper_R = None


def getJoystick():
    joystick = Joystick(0)

    # Button assignments
    button_A = JoystickButton(joystick, 1)
    button_B = JoystickButton(joystick, 2)
    button_X = JoystickButton(joystick, 3)
    button_Y = JoystickButton(joystick, 4)
    bumper_L = JoystickButton(joystick, 5)
    bumper_R = JoystickButton(joystick, 6)
    button_back = JoystickButton(joystick, 7)
    button_start = JoystickButton(joystick, 8)
    stick_L = JoystickButton(joystick, 9)
    stick_R = JoystickButton(joystick, 10)

    # Command assignments
    button_A.whileHeld(LowerLift())
    button_X.whenPressed(SetDriveSpeed(0.4))
    button_Y.whenPressed(SetDriveSpeed(1.0))
    bumper_L.whileHeld(HoldLift())
    bumper_R.whileHeld(RaiseLift())
    button_back.whileHeld(DislodgeBox())
    button_start.whileHeld(RaiseTaster())
    stick_L.whileHeld(LowerTaster())
    stick_R.whileHeld(RaiseWinch())

    return joystick
