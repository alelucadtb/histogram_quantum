import matplotlib.pyplot as plt
import numpy as np
import utils as ut
from scipy.stats import norm

# Read the file
f = open('/Users/alelucatello/Documents/Unipd/Quantum/lab1_repo/data_txt/x0a0y0b0.txt','r')

# Creating two vector for putting the values of the times arrival of the photons for the channels
times = []
channel = []
# To create the vector for store the difference between the times arrival 
data = []

# Reading the lines in .txt file and save the data 
for line in f:
    photon = line.split()
    times.append(ut.convert_to_int(photon[0]))
    channel.append(ut.convert_to_int(photon[1]))

for i in range(len(channel) - 1):
    if channel[i] == channel[i+1]:
        continue
    elif channel[i] < channel[i+1]:
        diff = ut.convert_to_time(times[i] - times[i+1])
        data.append(diff)
    else:
        diff = ut.convert_to_time(times[i+1] - times[i])
        data.append(diff)

# Fit a normal distribution to the data: mean and standard deviation
mu, std = norm.fit(data)

# Plotting the histogram
plt.hist(data, bins=50, color='skyblue', edgecolor='black')

# Plot the PDF
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 200)
p = norm.pdf(x, mu, std)

mu_ns = mu * 1e9
std_ns = std * 1e9

plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values: μ = {:.2f} ns, σ = {:.2f} ns".format(mu_ns, std_ns)
plt.title(title)

# Adding labels and title
plt.xlabel('Difference in time arrival (s)')
plt.ylabel('Pairs of photons')

# Display the plot
plt.show()





