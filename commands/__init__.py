import inputs.oi as oi
import robotmap
from .pneumatics.solenoid_extend import SolenoidExtend
from .pneumatics.solenoid_retract import SolenoidRetract
from .pneumatics.solenoid_halt import SolenoidHalt

def init():
    oi.A.whenPressed(SolenoidExtend())
    oi.B.whileHeld(SolenoidRetract())
    oi.B.whenReleased(SolenoidHalt())
    oi.X.whenPressed(SolenoidHalt())
