import matplotlib.pyplot as plt
import numpy as np
import utils as ut

# Read the file
f = open('/Users/alelucatello/Documents/Unipd/Quantum/lab1_repo/data_txt/x1a0y0b1.txt','r')

# Creating two vector for putting the values of the times arrival of the photons for the channels
times1 = []
times2 = []
# To create the vector for store the difference between the times arrival 
data = []


# Reading the lines in .txt file and save the data 
for line in f:
    photon = line.split() # Set the space ' ' as a divider for the data
    float_value = float(photon[1])  # Convert the string to a float
    int_value = int(float_value)
    if int_value == 1:
        times1.append(ut.convert_to_int(photon[0]))
    else:
        times2.append(ut.convert_to_int(photon[0]))

for element1 in times1:
    diff, index = ut.find_min_diff(times2, element1)
    if index == None:
        continue
    else:
        diff_s = diff * 81e-12
        data.append(diff_s)
        times2.pop(index) # Remove the couple of photons that arrive at the same time

# Plotting the histogram
plt.hist(data, bins=50, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Difference in time arrival (s)')
plt.ylabel('Pairs of photons')

# Display the plot
plt.show()





