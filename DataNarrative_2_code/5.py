import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#question 5: Compensation salary for urban areas are given generally high. Using the data set show that which areas are more developed
# To find the mean salary in a particular states
place_salary = dff.groupby('State')['Average compensation - all ranks'].mean()

# To plot a bar graph of the mean values
place_salary.plot(kind='bar', figsize=(10, 10))
plt.xlabel('State(Postal code)')
plt.ylabel('Average compensation salary for all ranks')
plt.title('Average compensation salary ')
plt.show()





