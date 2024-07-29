import matplotlib.pyplot as plt
import numpy as np
import utils as ut

# Read the file
f = open('/Users/alelucatello/Documents/Unipd/Quantum/lab1_repo/data_txt/x0a0y0b0.txt','r')

# Creating two vector for putting the values of the time arrival of the photons for the channels
times1 = []
times2 = []
# Creating variables for the min difference
min_diff = float('inf')
closest_element = None
data = []

# Reading the lines in .txt file and save the data 
for line in f:
    photon = line.split() # Set the space ' ' as a divider for the data
    float_value = float(photon[1])  # Convert the string to a float
    int_value = int(float_value)
    if int_value == 1:
        times1.append(ut.convert_to_float(photon[0]))
    else:
        times2.append(ut.convert_to_float(photon[0]))

# Iterate through the list
for element1 in times1:
    closest = ut.find_closest_element(times2, element1)
    data.append(closest)

# Plotting a basic histogram
plt.hist(data, bins=400, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Value of the difference')
plt.ylabel('Pair of photons')
plt.title('Basic Histogram')

# Display the plot
plt.show()





