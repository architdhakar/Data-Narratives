import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#Question 10: Find the number of top 20 most expensive colleges and verify that expensiveness of college is directly proportion to its graduation rate in general. Also do same of top 20 least expensive colleges
#(a)
# To sum all the cost in diffrent activities in a college
df['Total Cost'] = df['In-state tuition'] + df['Out-of-state tuition'] + df['Room and board costs'] + df['Room costs'] + df['Board costs'] + df['Additional fees'] + df['Estimated book costs'] + df['Estimated personal spending']

# To sort the data set on the basis of its total cost in decreasing order
top20_expensive_colleges = df.sort_values('Total Cost', ascending=False).head(20)

# To Plot the bar graph for different cost factors for the top 20 most expensive colleges
plt.figure().set_figwidth(30)
top20_expensive_colleges[['College name', 'In-state tuition', 'Room and board costs', 'Room costs', 'Board costs', 'Additional fees', 'Estimated book costs', 'Estimated personal spending']].set_index('College name').plot(kind='bar', stacked=True)
plt.ylabel('Cost')
plt.title('Top 20 expensive colleges')
plt.show()

# To plot the graduation rate for these top 20 colleges
plt.bar(top20_expensive_colleges['College name'], top20_expensive_colleges['Graduation rate'])
plt.xticks(rotation=90)
plt.xlabel('College name')
plt.ylabel('Graduation rate')
plt.title('Graduation rate by College')

# Show the plot
plt.show()

# (b)

# To sum all the cost in diffrent activities in a college
df['Total Cost'] = df['In-state tuition'] + df['Out-of-state tuition'] + df['Room and board costs'] + df['Room costs'] + df['Board costs'] + df['Additional fees'] + df['Estimated book costs'] + df['Estimated personal spending']

# To sort the data set on the basis of its total cost in increasing order to find least expensive colleges
top20_expensive_colleges = df.sort_values('Total Cost', ascending=True).head(20)

# To Plot the bar graph for different cost factors for the top 20 least expensive colleges
top20_expensive_colleges[['College name', 'In-state tuition', 'Room and board costs', 'Room costs', 'Board costs', 'Additional fees', 'Estimated book costs', 'Estimated personal spending']].set_index('College name').plot(kind='bar', stacked=True)
plt.ylabel('Cost')
plt.title('Top 20 least Expensive Colleges')
plt.show()

# To plot the graduation rate for these top 20 least expensive colleges
plt.bar(top20_expensive_colleges['College name'], top20_expensive_colleges['Graduation rate'])
plt.xticks(rotation=90)
plt.xlabel('College name')
plt.ylabel('Graduation rate')
plt.title('Graduation rate by College')

# Show the plot
plt.show()




