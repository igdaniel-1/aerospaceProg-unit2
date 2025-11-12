# Unit 2 Question 2 part A

# Planetary Analysis with Pandas

# Objectives:
# Create a Pandas Series representing distances of planets from the Sun (in million kilometers)
# Create a Pandas DataFrame representing characteristics of moons of the outer planets
# Analyze the data to find key information about planetary distances and moon characteristics

import pandas as pd
import numpy as np


planet_distances = { #(in million kilometers)
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.6,
    'Saturn': 1433.5,
    'Uranus': 2872.5,
    'Neptune': 4495.1,
    'Pluto': 5906.4
}

moon_data = {
    'Planet': ['Jupiter', 'Jupiter', 'Saturn', 'Saturn', 'Uranus', 'Neptune'],
    'Moon': ['Io', 'Ganymede', 'Titan', 'Rhea', 'Titania', 'Triton'],
    'Diameter (km)': [3642, 5262, 5150, 1528, 1578, 2707],
    'Orbital Period (days)': [1.77, 7.15, 15.95, 4.52, 8.71, 5.88]
}

# Pandas Series representing distances of planets from the Sun
distanceSun = np.array(planet_distances)
distanceSunSeries = pd.Series(distanceSun)
print("\nSun Distance Series from NumPy array:")
print(distanceSunSeries)

# Pandas DataFrame representing characteristics of moons of the outer planets
infoMoonDF = pd.DataFrame(moon_data)
print("\nMoon Info DataFrame created from Moon Info Series:")
print(infoMoonDF)

# Analyze the data to find key information about planetary distances and moon characteristics
# Planetary Distances DF
planetDistanceLessThan250 = [key for key, val in planet_distances.items() if val < 250]
print("\nPlanets Between the Sun and the Asteroid Belt:")
print(planetDistanceLessThan250)

# Moon Characteristics DF
moonsJupiter = infoMoonDF[infoMoonDF['Planet']=='Jupiter']
print("\nData Frame filtered to display the Moons of Jupiter:")
print(moonsJupiter)
