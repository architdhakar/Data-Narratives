import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#Question 11: Plot the student/faculty ratio and from that conclude that colleges with lower student/faculty ratio have higher graduation rates

#To extract particular column
ratio= df['Student/faculty ratio'].dropna()
plt.hist(ratio, bins=20)
plt.title('Student/Faculty Ratio distribution')
plt.xlabel('Ratio')
plt.ylabel('Count')
plt.show()

# To drop the values with * 
data1 = df.dropna(subset=['Student/faculty ratio'])

# To Sort the dataframe by student/faculty ratio in ascending order
data1_sort = data1.sort_values(by=['Student/faculty ratio'])

# To Select the top 20 colleges having lower student/faculty ratio
df_top_20 = data1_sort.iloc[:20]

# To plot Scatter
plt.scatter(df_top_20['College name'], df_top_20['Student/faculty ratio'])
plt.title('Top 20 Colleges by Student/Faculty Ratio')
plt.xlabel('College Name')
plt.ylabel('Student/Faculty Ratio')
plt.xticks(rotation=90)
plt.show()

# To extract top colleges
top_colleges = data1_sort.iloc[:20]

# To plot PDF plot
sns.displot(data=top_colleges, x='Graduation rate', kind='kde')
plt.title('PDF of Graduation Rate for Top 20 colleges based on Student/Faculty Ratio')
plt.xlabel('Graduation Rate')
plt.ylabel('Probability')
plt.show()





