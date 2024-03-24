# Question 2   FrenchOpen men's match 2013
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
# To Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\FrenchOpen-men-2013.csv")
# To extract the needed columns from the data column
breaks_created_p1 = df["BPC.1"].values
breaks_won_p1 = df["BPW.1"].values
breaks_created_p2 = df["BPC.2"].values
breaks_won_p2 = df["BPW.2"].values
# Converting above columns in array to calculate the covariance matrix
breaks_data = np.array([breaks_created_p1, breaks_won_p1, breaks_created_p2, breaks_won_p2])
# Calculate the covariance matrix
cov_matrix = np.cov(breaks_data)
print("            Covariance matrix")
print(cov_matrix)