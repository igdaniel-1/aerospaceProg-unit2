# Unit 2 Question 2 part B
# Deeper Dive into SpaceX Launch Dataset 

# Objectives:
# Reinitialize the dataframe and name it launches_dataset
# View the first values of the dataset using the head() method
# Print out the "Customer Country" column
# Print out all the unique customer countries
# Make a variable named launches_by_country and make it grouped by the "Customer Country" column
# Print out all the launches with a payload mass ("Payload Mass (kg)") of less than 4000
# Print the median payload mass for United States

import pandas as pd

# load data
space_x_missions_csv = "https://raw.githubusercontent.com/BriantOliveira/SpaceX-Dataset/master/dataset/SpaceX-Missions.csv"
launches_dataset = pd.read_csv(space_x_missions_csv)
print("\nHead of document:")
print(launches_dataset.head())

# Print out the "Customer Country" column
customerCountryColumn = launches_dataset['Customer Country']
print("\nCustomer Country:")
print(customerCountryColumn)

# Print out all the unique customer countries
print("\nUnique Countries from Customer Country column:")
print(pd.unique(launches_dataset["Customer Country"]))

# Make a variable named launches_by_country and make it grouped by the "Customer Country" column
launches_by_country = launches_dataset.groupby("Customer Country")
launches_by_country.head()
print("\nLaunches by Country")
print(launches_by_country)

# Print out all the launches with a payload mass ("Payload Mass (kg)") of less than 4000
print("\nLess than 4000kg payload mass:")
print(launches_dataset[launches_dataset['Payload Mass (kg)']<4000])

# Print the median payload mass for United States
print("\nMedian Payload Mass of United States launches:")
medianOfAmericanLaunches = launches_dataset[launches_dataset['Customer Country'] == "United States"]['Payload Mass (kg)'].median()
# The above line can be decomposed into the following 2 lines for clarity
# americanLaunches = launches_dataset[launches_dataset['Customer Country'] == "United States"]
# medianOfAmericanLaunches = americanLaunches['Payload Mass (kg)'].median()
print(medianOfAmericanLaunches)