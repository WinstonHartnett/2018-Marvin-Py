from pyfrc.physics import drivetrains, motor_cfgs
from pyfrc.physics.units import units

class PhysicsEngine(physics_controller):
    
    def __init__(self, physics_controller):
        self.physics_controller = physics_controller
        self.position = 0
        bumper_width = 0 * units.inch
        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_CIM,           # motor configuration
            120 * units.lbs,                    # robot mass
            8.45,                              # drivetrain gear ratio
            2,                                  # motors per side
            22 * units.inch,                    # robot wheelbase
            26.5 * units.inch + bumper_width * 2, # robot width
            32 * units.inch + bumper_width * 2, # robot length
            8 * units.inch,                     # wheel diameter
        )        
    def update_sim(self, hal_data, now, tm_diff):
        self.physics_controller.drive(speed, rotation, tm_diff)
        l_motor1 = hal_data["pwm"][0]["value"]
        r_motor1 = hal_data["pwm"][2]["value"]

        x, y, angle = self.drivetrain.get_distance(l_motor1, r_motor1, tm_diff)
        self.physics_controller.distance_drive(x, y, angle)

        self.position += hal_data["pwm"][4]["value"] * tm_diff *

        
