#Question4
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
# To open the csv file
tennis_data = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\Wimbledon-women-2013.csv")
# To Find the player who lost in round 1
player_round1_loss = tennis_data[(tennis_data['Round'] == 1) & (tennis_data['Result'] == 0)].iloc[0]
# Find the player who played in the final round
player_finalist = tennis_data[tennis_data['Round'] == 7].iloc[0]
# Create a bar plot comparing the features of the two players
features = ['FSP.1', 'ACE.1', 'UFE.1', 'WNR.1', 'DBF.1', 'NPA.1']
player1_vals = [player_round1_loss[feature] for feature in features]
player2_vals = [player_finalist[feature] for feature in features]
x = range(len(features))

fig, ax = plt.subplots(figsize=(7, 5))
rects1 = ax.bar(x, player1_vals, width=0.35, color='blue', label='Round 1 Loser')
rects2 = ax.bar([i + 0.35 for i in x], player2_vals, width=0.35, color='red', label='Finalist')

ax.set_ylabel('Feature Values')
ax.set_title('Comparison of Wimbledon Womens player Features of 2013')
ax.set_xticks([i + 0.35 for i in x])
ax.set_xticklabels(features)
ax.legend()

plt.show()
