import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy as sp
#Questions5: Observe whether user have given fair ratings means user is trustworthy who have read the content.
file_path2="https://github.com/zygmuntz/goodbooks-10k/blob/master/ratings.csv?raw=true"
df=pd.read_csv(file_path2)       # To open the csv file
# data analysis for users
x=df.query('user_id==30944')['rating']      # To find the rating on diffrent books
x.head(10)
print(x)