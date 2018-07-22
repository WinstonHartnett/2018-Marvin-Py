from commands import com_drive as cd
from commands import com_intake as ci
from commands import com_lift as cl
from commands import com_taster as ct
from commands import com_winch as cw

from wpilib import SendableChooser, SmartDashboard
from wpilib.command import Scheduler, Command

import constants as c
import sub as s


class Dashboard():

    def __init__(self):
        pass

    def init(self):
        SmartDashboard.putData("Scheduled Commands", Scheduler.getInstance())
        SmartDashboard.putData("Drive Command", s.sub_drive)
        SmartDashboard.putData("Box Command", s.sub_intake)
        SmartDashboard.putData("Lift Command", s.sub_lift)
        SmartDashboard.putData("Winch Command", s.sub_winch)
        SmartDashboard.putData("Taster Command", s.sub_taster)
        SmartDashboard.putData("Top Limit", s.sub_lift.lim_top)
        SmartDashboard.putData("Bottom Limit", s.sub_lift.lim_bot)
        SmartDashboard.putNumber("Robot Location", c.loc_robot)
        SmartDashboard.putNumber("Auton Target", c.loc_target)
        SmartDashboard.putNumber("Wait Time", 0.0)
        SmartDashboard.putNumber("Lift Speed", c.spd_lift)
        SmartDashboard.putNumber("Taster Speed", c.spd_taster)
        SmartDashboard.putNumber("Rotate Speed", c.spd_rotate)
        SmartDashboard.putNumber("Winch Speed", c.spd_winch)

        self.c_winch = SendableChooser()
        self.c_lift = SendableChooser()
        self.c_taster = SendableChooser()
        self.c_drive = SendableChooser()
        self.cho_drive = cd.SetRotateSpeed(1.0)
        self.cho_lift = cl.SetLiftSpeed(1.0)
        self.cho_taster = ct.SetTasterSpeed(1.0)
        self.cho_winch = cw.SetWinchSpeed(1.0)

        self.c_lift.addDefault("Lift (10)",          cl.SetLiftSpeed(1.0))
        self.c_lift.addObject("Lift (8)",            cl.SetLiftSpeed(0.8))
        self.c_lift.addObject("Lift (6)",            cl.SetLiftSpeed(0.6))
        self.c_lift.addObject("Lift (4)",            cl.SetLiftSpeed(0.4))
        self.c_lift.addObject("Lift (2)",            cl.SetLiftSpeed(0.4))

        self.c_taster.addDefault("Taster (-5.3)",    ct.SetTasterSpeed(-0.53))
        self.c_taster.addObject("Taster (-3)",       ct.SetTasterSpeed(-0.33))
        self.c_taster.addObject("Taster (-2)",       ct.SetTasterSpeed(-0.2))
        self.c_taster.addObject("Taster (1)",        ct.SetTasterSpeed(0.1))
        self.c_taster.addObject("Taster (2)",        ct.SetTasterSpeed(0.2))

        self.c_winch.addDefault("Winch (10)",        cw.SetWinchSpeed(1.0))
        self.c_winch.addObject("Winch (8)",          cw.SetWinchSpeed(0.8))
        self.c_winch.addObject("Winch (5)",          cw.SetWinchSpeed(0.5))
        self.c_winch.addObject("Winch (-8)",         cw.SetWinchSpeed(-0.8))
        self.c_winch.addObject("Winch (-10)",        cw.SetWinchSpeed(-1.0))

        self.c_drive.addObject("Rotate (10)",        cd.SetRotateSpeed(1.0))
        self.c_drive.addObject("Rotate (8)",         cd.SetRotateSpeed(0.8))
        self.c_drive.addDefault("Rotate (6)",        cd.SetRotateSpeed(0.6))
        self.c_drive.addObject("Rotate (4)",         cd.SetRotateSpeed(0.4))

        # pass

    def poll(self):
        self.cho_taster = self.c_taster.getSelected()
        self.cho_lift = self.c_lift.getSelected()
        self.cho_drive = self.c_drive.getSelected()
        self.cho_winch = self.c_winch.getSelected()
        SmartDashboard.updateValues()

        # pass

    def start(self):
        self.cho_drive.start()
        self.cho_lift.start()
        self.cho_winch.start()
        self.cho_winch.start()

        # pass
