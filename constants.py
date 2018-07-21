import math

# Constants

distance_per_pulse = ((math.pi * 6) / 2048)
kp = 0.03

# Controllers
spark_front_left = int(1)
spark_front_right = int(2)
spark_back_left = int(3)
spark_back_right = int(4)

# Encoders
encoder_left_1 = int(0)
encoder_left_2 = int(1)
encoder_right_1 = int(2)
encoder_right_2 = int(3)

# Drive Speed Steps
spd_0 = float(0.0)
spd_2 = float(0.2)
spd_4 = float(0.4)
spd_6 = float(0.6)
spd_8 = float(0.8)
spd_10 = float(1.0)

# Default Variables
spd_drive = spd_6
spd_rotate = spd_6
spd_intake = spd_6
spd_lift = spd_6
spd_lift_lower = spd_4
spd_taster = spd_6
spd_winch = spd_6
