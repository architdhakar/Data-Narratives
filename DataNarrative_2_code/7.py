import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#Question 7: Show that maths is the scoring subject in the SAT exam as comparing to verbal exam in order to help the future SAT aspirants.

# To assign new variables to the needed columns
college_names = df.head(20)['College name']
math_scores = df.head(20)['Average Math SAT score']
verbal_scores = df.head(20)['Average Verbal SAT score']

# To Set the figure size
plt.figure(figsize=(10,5))

# To Plot the double bar graph
bar_width = 0.2
opacity = 0.8
index = range(len(college_names))
plt.bar(index, math_scores, bar_width, alpha=opacity, color='r', label='Average Maths SAT score')
plt.bar([i+bar_width for i in index], verbal_scores, bar_width, alpha=opacity, color='y', label='Average Verbal SAT score')

# To set labels
plt.xlabel('College name')
plt.ylabel('Average SAT Scores of Maths/Verbal')
plt.title('Comparison of Average Maths and Verbal SAT Scores for different colleges')

# To Add legend
plt.legend()

# To Add x-axis tick labels
plt.xticks([i + bar_width for i in index], college_names, rotation=90)
plt.show()



