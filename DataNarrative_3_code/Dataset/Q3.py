#question3 Aus Women's data
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns

# To Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\AusOpen-women-2013.csv")
# Create a scatter plot of unforced errors vs. unforced errors
plt.scatter(df["UFE.1"], df["UFE.2"], c=df["Result"])
#To Add a colorbar legend
plt.colorbar()
plt.xlabel("Player 1 Unforced Errors")
plt.ylabel("Player 2 Unforced Errors")
plt.title("Relationship between Unforced Errors for player 1 and player 2")
plt.show()

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\Users\Lenovo\Desktop\22110031_ES114_DN3\AusOpen-women-2013.csv")

# Calculate the average number of unforced errors made by winners and losers in each match
winners = df.loc[df["Result"] == 1]
losers = df.loc[df["Result"] == 0]
winner_avg_ue = winners["UFE.1"].mean()
loser_avg_ue = losers["UFE.1"].mean()
#To Create a bar plot of the average unforced errors made by winners and losers
plt.bar(["Winners", "Losers"], [winner_avg_ue, loser_avg_ue])
plt.xlabel("Match Outcome")
plt.ylabel("Average Unforced Errors")
plt.title("Average Unforced Errors by players")
plt.show()
