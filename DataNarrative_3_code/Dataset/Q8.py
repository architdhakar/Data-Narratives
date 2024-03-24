#Question 8
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns

# To open the csv data file
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\USOpen-men-2013.csv")

# Create a scatter plot between FSW.1 and SSW.1
plt.scatter(df['FSW.1'], df['SSW.1'])
plt.xlabel('First Serve Points Won Percentage')
plt.ylabel('Second Serve Points Won Percentage')
plt.title('Scatter Plot between First Serve Points Won and Second Serve Points Won')
plt.show()
