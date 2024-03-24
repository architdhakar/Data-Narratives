#Question 7
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns

# To open csv data
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\FrenchOpen-women-2013.csv")

# To Calculate the winner point difference
df['winner_diff'] = df['WNR.1'] - df['WNR.2']
# To Create a new column for the match outcome (1 if Player 1 wins, 0 otherwise)
df['win'] = (df['FNL.1'] > df['FNL.2']).astype(int)
# To Calculate the probability of Player 1 winning given higher number of winner points
p_win_given_winner_diff = df.loc[df['winner_diff'] > 0, 'win'].mean()
# To Create a list of probabilities for different values of winner_diff
probabilities = []
for i in range(30):
    df_sample = df.sample(frac=1, replace=True)
    p = df_sample.loc[df_sample['winner_diff'] > 0, 'win'].mean()
    probabilities.append(p)
import seaborn as sns
sns.displot(probabilities, kde=True, stat='density')
plt.xlabel('Probability')
plt.ylabel('Number of winner')
plt.title('Probability vs Number of winner')
plt.show()