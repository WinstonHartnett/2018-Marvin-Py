import robotmap
from inputs import oi

from .change_value import Change_Value
from .chassis_drive import Chassis_Drive
from .intake_dislodge import Intake_Dislodge
from .intake_eject import Intake_Eject
from .intake_intake import Intake_Intake
from .lift_hold import Lift_Hold
from .lift_move import Lift_Move
from .winch_raise import Winch_Raise


def init():
    oi.A.whileHeld(Lift_Move(False))
    oi.X.whenPressed(Change_Value(robotmap.spd_chassis_drive, 0.4))
    oi.Y.whenPressed(Change_Value(robotmap.spd_chassis_drive, 1.0))
    oi.bumper_L.whileHeld(Lift_Hold)
    oi.bumper_R.whileHeld(Lift_Move(True))
    oi.back.whileHeld(Intake_Dislodge)
    oi.stick_R.whileHeld(Winch_Raise)
