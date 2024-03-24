#question 6
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns

# To open the csv tennis dataset
tennis_data = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\Wimbledon-men-2013.csv")

# Calculate the average double faults committed for each round
rounds_df = tennis_data.groupby('Round')['DBF.1', 'DBF.2'].mean().reset_index()
rounds_df['Avg Double Faults'] = rounds_df[['DBF.1', 'DBF.2']].mean(axis=1)

# Plot a bar graph to visualize the trend
plt.bar(rounds_df['Round'], rounds_df['Avg Double Faults'])
plt.xlabel('Round')
plt.ylabel('Average Double Faults Committed')
plt.title('Trend of Average Double Faults Committed by Round')
plt.show()
