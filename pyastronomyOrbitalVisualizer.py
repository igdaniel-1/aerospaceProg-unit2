import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Orbital_Visualizer:
    def __init__(self, TLEFile):
        self.TLEFile = TLEFile
        self.name = ""
        self.line1 = "" 
        self.line2 = ""
        self.satellite = None
    def extract_tle_contents(self):
        tle_data = open(self.TLEFile, "r").readlines()
        # print(len(tle_data))

        # for a 3 line TLE
        if len(tle_data) == 3:
            self.name = tle_data[0]
            self.line1 = tle_data[1]
            self.line2 = tle_data[2]
            # print(self.name, self.line1, self.line2)

        # for a 2 line TLE
        elif len(tle_data) == 2:
            self.line1 = tle_data[0]
            self.line2 = tle_data[1]

def main():
    newOrbital = Orbital_Visualizer("tle.txt")
    newOrbital.extract_tle_contents()

main()