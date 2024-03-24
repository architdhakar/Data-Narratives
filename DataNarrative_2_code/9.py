import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#Question 9:(a) Make a prefrence list for the students who appeared in SAT exam on the basis of average marks to get addmission in that college.
preference_list= df.sort_values('Average Combined SAT score', ascending=False).head(20)

# to Create the scatter plot
plt.figure(figsize=(8,3))
plt.scatter(preference_list['College name'], preference_list['Average Combined SAT score'])
plt.title('Average SAT score of top 20 colleges')
plt.xlabel('College Name')
plt.xticks(rotation=90)
plt.ylabel('Average Combined SAT Score')
plt.show()

#(b)

preference_list1= df.sort_values('Average ACT score', ascending=False).head(20)

# to Create the scatter plot
plt.figure(figsize=(8,3))
plt.scatter(preference_list1['College name'], preference_list1['Average ACT score'])
plt.title('Average ACT score of top 20 colleges')
plt.xlabel('College Name')
plt.xticks(rotation=90)
plt.ylabel('Average Combined ACT Score')
plt.show()




