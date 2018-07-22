from subsystems import Sub_Drive, Sub_Intake, Sub_Lift, Sub_Taster, Sub_Winch


def init():
    global sub_drive
    global sub_intake
    global sub_lift
    global sub_taster
    global sub_winch

    sub_drive = Sub_Drive()
    sub_intake = Sub_Intake()
    sub_lift = Sub_Lift()
    sub_taster = Sub_Taster()
    sub_winch = Sub_Winch()

    sub_drive.setupEncoder()
