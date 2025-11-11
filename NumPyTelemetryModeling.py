# Unit 2 - Question 1
# Spacecraft Telemetry Modeling with NumPy Arrays

# Objectives:
# Generate a NumPy array representing time in seconds from t=0 to t=100 seconds with a step size of 1 second.
# Generate a NumPy array representing altitude in meters during the launch phase. The altitude should start at 0 meters and increase linearly with time at a constant rate of 100 meters per second.
# Calculate the velocity array using the altitude array. Assume constant acceleration due to gravity (9.81 m/s^2) during the launch phase.
# Calculate the acceleration array using a constant acceleration value of 9.81 m/s^2.
# Print the shape and data type of each generated NumPy array

import numpy as np

gravity_acceleration = 9.81  # Constant acceleration due to gravity in m/s^2



def exercise1():
    # data
    arr_time_100 = np.arange(101)
    arr_altitude = np.arange(0, 10000, 100)
    arr_velocity = arr_altitude*gravity_acceleration
    arr_acceleration = arr_velocity*gravity_acceleration

    print("Time:",arr_time_100)
    print("Time type:",type(arr_time_100[0]))

    print("Altitude:",arr_altitude)
    print("Altitude type:",type(arr_altitude[0]))

    print("Velocity:",arr_velocity)
    print("Velocity type:",type(arr_velocity[0]))

    print("Acceleration:",arr_acceleration)
    print("Acceleration type:",type(arr_acceleration[0]))

def exercise2():
    print("hey")
