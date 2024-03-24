import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
# Question 2: Using the given dataset show that colleges who pays more to their professors are tier 1 colleges

# To define the data set
url1='http://lib.stat.cmu.edu/datasets/colleges/aaup.data'
dff1=pd.read_csv(url1)      # To read the CSV file 
dff1.columns = ['FICE', 'College name','State', 'Type','Average salary - full professors','Average salary - Associate professors', 'Average salary - assistant professors','Average salary - all ranks','Average compensation - full professors','Average compensation - associate professors','Average compensation - assistant professors','Average compensation - all ranks','Number of full professors','Number of associate professors','Number of assistant professors','Number of instructors','Number of faculty - all ranks']

# To sort the values on the basis of all rank salary and full professor salaary
df5=dff1.sort_values(by='Average salary - all ranks')
# To print the above data
print(df5.tail(10)['Type'])
print(df5.head(10)['Type'])

fig, ax = plt.subplots(figsize=(10,6))

# To Plot the data for maximum average salary by colleges and their types
ax.plot(df5.head(15)['College name'], df5.head(15)['Average salary - all ranks'], label='Type-IIB', color='blue')

#To Plot the data for minimum average salary by colleges and their types
ax.plot(df5.tail(15)['College name'], df5.tail(15)['Average salary - all ranks'], label='Type-I', color='red')
ax.set_xlabel('College Name')
ax.set_ylabel('Average Salary')
ax.set_title('Comparison of Average Salaries- All ranks')
plt.xticks(rotation=90)
ax.legend()
plt.show()