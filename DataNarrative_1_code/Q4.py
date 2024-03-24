import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy as sp
#Question4 : User who have read/rated maximum number of books
file_path2="https://github.com/zygmuntz/goodbooks-10k/blob/master/ratings.csv?raw=true"
print("1. User(id) who have read/rated maximum number of books")
df=pd.read_csv(file_path2) #To open the csv file
df1=df["user_id"].mode()    #To access the user id column
print(df1)
print()

# From the output we can observe that user with id 12874 and 30944 have rated/read maximum no of books
df2=df["user_id"].value_counts().max()
print("2. No of books read/rated by the user with maximum reads is",df2)

# From above data analysis we can improve the goodread book store's bussiness by giving some points to the top user , so that he 
# can use those points to buy some books. This analysis can help to improve the bussiness of Goodread books store.