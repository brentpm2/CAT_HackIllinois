import os
import numpy as np
import h5py
import matplotlib.pyplot as plt

from scipy.stats import pearsonr
from numpy.lib.function_base import average
# seed random number generator

cwd = os.getcwd()

#Open the data file
filepath = cwd + '\\demo.hdf'
f = h5py.File(filepath, 'r')


#Show all channels available in file
chanIDs = f['DYNAMIC DATA']
#total channels per file

print("Total channels per file: {}".format(len(chanIDs)))

#max, min, avg of each channel
data_points = 0
for channel in chanIDs:
    channel_data = chanIDs[channel]['MEASURED']
    data_points += len(channel_data)
    print("Channel: {}\tMax: {}\tMin: {}\tAverage: {}\tData points: {}".format(channel,max(channel_data),min(channel_data),average(channel_data),len(channel_data)))
    print(data_points)
print("Total data points: ".format(data_points))

#Plot a sample dataset
ChannelNameA = 'ch_0'
ChannelNameB = 'ch_10'
dset1 = chanIDs[ChannelNameA]['MEASURED']
dset2 = chanIDs[ChannelNameB]['MEASURED']

corr, _ = pearsonr(dset1, dset2)
print('Pearsons correlation: %.3f' % corr)

#Plot a sample dataset
plt.plot(np.arange(len(dset1[()])), dset1[()],np.arange(len(dset2[()])),dset2[()]) # plotting by columns
plt.title("plot of ch0 and ch10")
plt.xlabel("Datapoint #")
plt.ylabel("Value")
plt.show()


#Close the file
f.close()