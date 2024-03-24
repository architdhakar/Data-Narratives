#Question 5
import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
# To open the csv file
tennis_data = pd.read_csv(r"C:\Users\Lenovo\Desktop\22110031_ES114_DN3\USOpen-women-2013.csv")

# To extract the relevant columns
winners = tennis_data['WNR.1'].values
unforced_errors = tennis_data['UFE.1'].values
# reshape the winners array
x = winners.reshape((-1, 1))
y = unforced_errors
# apply linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('Coefficient of determination:', r_sq)
print('Slope:', model.coef_[0])
# plot the data and the regression line
plt.scatter(x, y, alpha=0.5)
plt.plot(x, model.predict(x), color='red')
plt.title("Number of winners vs. Unforced errors")
plt.xlabel("Number of winners")
plt.ylabel("Unforced errors")
plt.show()