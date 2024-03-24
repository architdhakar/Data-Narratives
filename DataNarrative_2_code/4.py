import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
# Question 4: Show that average compensation for full professors is not the good criteria to join the college by some new professors

# To define the dataset
url1='http://lib.stat.cmu.edu/datasets/colleges/aaup.data'
dff=pd.read_csv(url1,na_values=['*'])      # To read the CSV file 
dff.columns = ['FICE', 'College name','State', 'Type','Average salary - full professors','Average salary - Associate professors', 'Average salary - assistant professors','Average salary - all ranks','Average compensation - full professors','Average compensation - associate professors','Average compensation - assistant professors','Average compensation - all ranks','Number of full professors','Number of associate professors','Number of assistant professors','Number of instructors','Number of faculty - all ranks']

# To plot the line graph for all ranks and professors
plt.plot(dff.head(20)['College name'], dff.head(20)['Average compensation - all ranks'], label='Average compensation - all ranks')
plt.plot(dff.head(20)['College name'], dff.head(20)['Average compensation - full professors'], label='Average compensation - full professors')
plt.xticks(rotation=90)
plt.xlabel('College name')
plt.ylabel('Average compensation salary')
plt.title('comparision on the basis of average compensation salary')
plt.legend()
plt.show()





