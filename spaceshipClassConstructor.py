# Unit 2 Question 4

# Spaceship OOP

# Objectives:
# Create a class called Spaceship
# Create a constructor for the class which takes a name, crew capacity, and speed.
# Set the instance variables of the class for each of the inputted constructor variables
# Create a method named increase_speed that increases the speed of the spaceship by 10 and prints it out
# Create a method named set_crew_capacity which takes a capacity value that prints out BOTH the previous and new capacity values
# Create a method named state_name which prints out the name of the spaceship

class Spaceship:
    def __init__(self, name, crewSize, speed):
        self.name = name
        self.crewSize = crewSize
        self.speed = speed
    def increase_speed(self, speed):
        self.speed = speed
        print("New speed is", self.speed, "km/hour.")
    def set_crew_capacity(self, crewSize):
        print("Previous crew capacity was", self.crewSize, "astronauts.")
        self.crewSize = crewSize
        print("New crew capacity is now", self.crewSize, "astronauts.")
    def state_name(self):
        print("The spaceship is named",self.name)

def main():
    newShip = Spaceship("SS Space", 8, 1000)
    newShip.state_name()
    newShip.increase_speed(1100)
    newShip.set_crew_capacity(12)

main()