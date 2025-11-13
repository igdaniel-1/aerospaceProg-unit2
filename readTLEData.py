# Unit 2 Question 5 part 1

# Reading Two-Line Element Set Data for Orbital Visualization of a Satellite 
# Data is fed from unit2/tle.txt

import math

path = "tle.txt"
tle_data = open("tle.txt", "r").readlines()
# print(tle_data)

# Remove end characters
# map function, example: map(function, iterable,..)
tle_data_clean = list(map(lambda line: line.strip(), tle_data))
# print(tle_data_clean)


# below this comment, I directly use AngelinaTsuboi's code, the author of this course
# source: https://github.com/ANG13T/python-for-aerospace/blob/main/Chapter%202%20-%20Libraries%20and%20Data%20Visualization/Lesson_5_TLE_Visualization.ipynb

# Interpreting the TLE lines as their indiv data points
for i in range(len(tle_data_clean)):
    
    name = tle_data_clean[0]
    line1 = tle_data_clean[1]
    line2 = tle_data_clean[2]

    # Extracting individual values from Line 2
    satellite_number = int(line1[2:7])
    classification = line1[7]
    international_designator_year = int(line1[9:11])
    international_designator_launch_number = int(line1[11:14])
    international_designator_piece_of_launch = line1[14:17]
    epoch_year = int(line1[18:20])
    epoch_day = float(line1[20:32])
    first_derivative_mean_motion = float(line1[33:43])
    second_derivative_mean_motion = line1[45:52]
    bstar_drag_term = line1[53:61]
    ephemeris_type = int(line1[62])
    element_number = int(line1[64:68])

    # Extracting individual values from Line 3
    inclination = float(line2[8:16])
    raan = float(line2[17:25])
    eccentricity = float("0." + line2[26:33])
    argument_of_perigee = float(line2[34:42])
    mean_anomaly = float(line2[43:51])
    mean_motion = float(line2[52:63])
    revolution_number = int(line2[63:68])

data = {
    "name": name, 
    "satellite_number": satellite_number, 
    "classification": classification, 
    "international_designator_year": international_designator_year, 
    "international_designator_launch_number": international_designator_launch_number, 
    "international_designator_piece_of_launch": international_designator_piece_of_launch,
    "epoch_year": epoch_year, 
    "epoch_day": epoch_day, 
    "first_derivative_mean_motion": first_derivative_mean_motion, 
    "second_derivative_mean_motion": second_derivative_mean_motion, 
    "bstar_drag_term": bstar_drag_term, 
    "ephemeris_type": ephemeris_type, 
    "element_number": element_number, 
    "inclination": inclination, 
    "raan": raan, 
    "eccentricity": eccentricity, 
    "argument_of_perigee": argument_of_perigee,
    "mean_anomaly": mean_anomaly, 
    "mean_motion": mean_motion,
    "revolution_number": revolution_number
}

# pretty print
def print_tle(satellite):
    print(f"Name: {satellite['name']}")
    print(f"Satellite Number: {satellite['satellite_number']}")
    print(f"Classification: {satellite['classification']}")
    print(f"International Designator Year: {satellite['international_designator_year']}")
    print(f"International Designator Launch Number: {satellite['international_designator_launch_number']}")
    print(f"International Designator Piece of Launch: {satellite['international_designator_piece_of_launch']}")
    print(f"Epoch Year: {satellite['epoch_year']}")
    print(f"Epoch Day: {satellite['epoch_day']}")
    print(f"First Derivative Mean Motion: {satellite['first_derivative_mean_motion']}")
    print(f"Second Derivative Mean Motion: {satellite['second_derivative_mean_motion']}")
    print(f"Bstar Drag Term: {satellite['bstar_drag_term']}")
    print(f"Ephemeris Type: {satellite['ephemeris_type']}")
    print(f"Element Number: {satellite['element_number']}")
    print(f"Inclination: {satellite['inclination']}")
    print(f"RAAN: {satellite['raan']}")
    print(f"Eccentricity: {satellite['eccentricity']}")
    print(f"Argument of Perigee: {satellite['argument_of_perigee']}")
    print(f"Mean Anomaly: {satellite['mean_anomaly']}")
    print(f"Mean Motion: {satellite['mean_motion']}")
    print(f"Revolution Number: {satellite['revolution_number']}")
    print()

# print full satellite data from TLE
# print_tle(data)


# Calculating Semi Major Axis
def semi_major_axis(mean_motion):
    G = 6.674 * 10**-11  # Gravitational constant (m³ kg⁻¹ s⁻²)
    M = 5.972 * 10**24   # Mass of the Earth (kg)
    n = mean_motion * (2 * math.pi) / (24 * 60 * 60)  # Convert mean motion from rev/day to rad/s
    return (G * M / (n**2))**(1/3)
semimajor_axis = semi_major_axis(data["mean_motion"])
# print(semimajor_axis)

# Calculating Orbital Period
def orbital_period(semi_major_axis):
    G = 6.674 * 10**-11  # Gravitational constant (m³ kg⁻¹ s⁻²)
    M = 5.972 * 10**24   # Mass of the Earth (kg)
    return 2 * math.pi * math.sqrt(semi_major_axis**3 / (G * M))
period = orbital_period(semimajor_axis)
# print(period)