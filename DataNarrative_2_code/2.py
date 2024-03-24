import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#Question 2: Find that which state has more no of tier 1 colleges
# TO count no of colleges of diffrent type in a state
state_count = dff.groupby(['State', 'Type']).size()
state_count = state_count.reset_index().set_index('State').pivot(columns='Type')
# To plot a grouped bar graph 
# stack is used to place graphs on one another
state_count.plot(kind='bar', stacked=True,figsize=(10, 10))

plt.xlabel('State(Postal code)')
plt.ylabel('Number of colleges')
plt.title('Colleges in state and its types')
plt.show()