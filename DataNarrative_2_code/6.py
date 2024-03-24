import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
import random
import seaborn as sns
#Question 6: Show that student prefer public colleges more than private colleges
url = 'http://lib.stat.cmu.edu/datasets/colleges/usnews.data'

# To read the csv file
df = pd.read_csv(url,na_values=['*'])

# To define the coloumn names to csv file
df.columns=['FICE', 'College name','State','Public/private','Average Math SAT score','Average Verbal SAT score','Average Combined SAT score','Average ACT score','First quartile - Math SAT','Third quartile - Math SAT','First quartile - Verbal SAT','Third quartile - Verbal SAT','First quartile - ACT','Third quartile - ACT','Number of applications received','Number of applicants accepted','Number of new students enrolled','Pct. new students from top 10% of H.S. class','Pct. new students from top 25% of H.S. class','Number of fulltime undergraduates','Number of parttime undergraduates','In-state tuition','Out-of-state tuition','Room and board costs','Room costs','Board costs','Additional fees','Estimated book costs','Estimated personal spending','Pct. of faculty with Ph.D','Pct. of faculty with terminal degree','Student/faculty ratio','Pct.alumni who donate','Instructional expenditure per student','Graduation rate']

# TO seperate the elements on the basis of public and private colleges
grouped = df.groupby('Public/private')['Number of applications received'].sum()

# Plot the pie chart
plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%')
plt.title('Comparision of applications recieved in public and private colleges. Public=1 Private=2')
plt.show()




