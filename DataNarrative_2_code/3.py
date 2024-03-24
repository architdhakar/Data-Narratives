import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
# Question 3: For a randomly selected college find the faculty division and reason the observation that in general every college have more no of associate professors
import random
# To select a random college
random_college = dff.loc[random.randint(0, len(dff)-1)]

# To categorise the different faculties on the basis of their division
faculty_count = [random_college['Number of full professors'], random_college['Number of associate professors'],
                  random_college['Number of assistant professors'], random_college['Number of instructors']]

# To plot a pie chart 
labels = ['Full professors', 'Associate professors', 'Assistant professors', 'Instructors']
plt.pie(faculty_count, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Faculty breakdown in ' + random_college['College name'])
plt.show()
