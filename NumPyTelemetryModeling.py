# Unit 2 - Question 1 exercises 1 and 2

# Exercise 1
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
    arr_time_100 = np.arange(0,101,1)

    # make altitude array out of shape of time array filled with zeros
    arr_altitude = np.zeros(arr_time_100.shape)
    # Increase altitude linearly with time (100 meters per second)
    arr_altitude += 100*arr_time_100

    arr_velocity = arr_time_100*gravity_acceleration
    arr_acceleration = np.full(arr_time_100.shape, gravity_acceleration)

    print("Time:",arr_time_100)
    print("Time type:",type(arr_time_100[0]))

    print("Altitude:",arr_altitude)
    print("Altitude type:",type(arr_altitude[0]))

    print("Velocity:",arr_velocity)
    print("Velocity type:",type(arr_velocity[0]))

    print("Acceleration:",arr_acceleration)
    print("Acceleration type:",type(arr_acceleration[0]))


# U2Q1 Exercise 2: Mission Profiling
# Objectives:
# Use NumPy's random number generation functions to generate simulated altitude, velocity, and acceleration data.
# Assume that the flight data consists of 1000 data points each for altitude, velocity, and acceleration.
# Perform array indexing and slicing to extract subsets of data for analysis.
# Use array comparisons and conditional methods to identify critical points:
# Critical altitude: Altitude above 5000 meters.
# Critical velocity: Velocity greater than 300 meters per second.
# Critical acceleration: Acceleration less than -9.8 meters per second squared (indicating deceleration).
# Concatenate arrays representing critical points to an array and print it out!


def exercise2():
    arr_rand_altitude = np.random.uniform(0, 10000, size=1000)
    arr_rand_velocity = np.random.uniform(0, 300, size=1000)
    arr_rand_acceleration = np.random.uniform(-20, 20, size=1000)

    # indicesAltitude = np.where(arr_rand_altitude > 5000)  <-- this method returns the indices instead of the values at those indices
    # indicesVelocity = np.where(arr_rand_velocity > 300)
    # indicesAcceleration = np.where(arr_rand_acceleration < -9.8)
    
    criticalAltitude = arr_rand_altitude[arr_rand_altitude > 5000]  #this method returns the values at the indices
    criticalVelocity = arr_rand_velocity[arr_rand_velocity > 300]
    criticalAcceleration = arr_rand_acceleration[arr_rand_acceleration < -9.8]

    flight_profile = np.concatenate((criticalAltitude, criticalVelocity, criticalAcceleration))
    print("Flight Profile: \n")
    print(flight_profile)

def main():
    exercise2()

main()