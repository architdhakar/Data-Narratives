import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#Question 8: Draw a PDF plot to show that a randomly selected college will have graduation rate atleast 75%
# import seaborn library
import seaborn as sns
# To extract the graduation column
grad_rate = df['Graduation rate']

# To find the no of colleges with graduation rate atleast 75
p = sum(grad_rate >= 75) / len(grad_rate)
print("Probability that a randomly selected college will be have graduation rate atleast 75%:", p)
# To plot the probability density function
sns.histplot(grad_rate, kde=True,stat='density')

# To define the labels
plt.xlabel('Graduation rate')
plt.ylabel('PDF')
plt.title('Probability Density Function(PDF) of Graduation Rate(%)')
plt.show()



