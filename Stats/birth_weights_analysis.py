# imports
import numpy as np
from matplotlib import pyplot as plt
# data

birth_weights = [ 5.8, 7.9, 8.7, 7.9, 7.3, 7.1, 7.6,
                7.4, 7.8, 7.2, 5.9, 6.4, 6.8, 6.9, 7.0, 6.7,
                9.2, 7.9, 6.1, 7.0, 7.4, 7.0, 6.9, 7.0,
                7.0, 7.7, 7.2, 7.8, 8.2, 8.1, 6.4, 7.4, 
                8.5, 9.0, 7.1, 7.2, 9.1, 8.0, 7.8, 8.2,
                7.6, 7.1, 7.2, 7.5, 7.3, 7.5, 8.7, 7.2]


# find the mean and median
birth_weight_mean = np.mean(birth_weights)
birth_weight_median = np.median(birth_weights)

print("The mean of birth weights is: " + str(birth_weight_mean))
print("The median of birth weights is: " + str(birth_weight_median))

# clean the data to find frequency
unique_elements, counts_elements = np.unique(birth_weights, return_counts=True)
print("Frequency of unique values: ")
print(np.array((unique_elements, counts_elements)))

# plot the data
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x_plot = unique_elements
y_plot = counts_elements
plt.xlabel("Weight in Pounds")
plt.ylabel("Frequency")
ax.bar(x_plot, y_plot)
plt.show()
