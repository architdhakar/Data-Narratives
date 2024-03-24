# Question1
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
# To load the CSV file into a pandas dataframe
data = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\AusOpen-men-2013.csv")

# calculate the correlation coefficient between first serve percentage and first serve win percentage
corr = data['FSP.1'].corr(data['FSW.1'])
print(corr)
# plot the correlation coefficient
plt.scatter(data['FSP.1'], data['FSW.1'])
plt.title(f"Correlation Coefficient: {corr:.2f}")
plt.xlabel('First Serve Percentage')
plt.ylabel('First Serve Points Won')
plt.show()