# import required libraries
import h5py as h5
import numpy as np
import matplotlib.pyplot as plt

# Read H5 file
f = h5.File("best_0.h5", "r")
# Get and print list of datasets within the H5 file
datasetNames = [n for n in f.keys()]
for n in datasetNames:
    print(n)

datasetValues = [n for n in f.values()]

for val in datasetValues:
    print(val)

model_weights = f['model_weights']
# extract one pixel from the data


optimizer_weights = f['optimizer_weights']



# Plot
plt.plot(model_weights, optimizer_weights)
plt.show()
