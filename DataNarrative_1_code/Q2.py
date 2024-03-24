import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy as sp
# Question 2 : Most popular categories book tags
file_path3="https://github.com/zygmuntz/goodbooks-10k/raw/master/samples/book_tags.csv"
file_path4="https://github.com/zygmuntz/goodbooks-10k/raw/master/tags.csv"
df=pd.read_csv(file_path3) #To open the csv file of book tags
df2=pd.read_csv(file_path4)         #To open the csv file of tags
df1=df.head(7)                                                  #To show the most popular tag_id
X=[]
for i in df1["tag_id"]:
    if i in df2["tag_id"]:
        x=df2.loc[df2['tag_id'] == i, 'tag_name'].item()
        X.append(x)
df1["tag_ids"]=pd.DataFrame(X)
print(df1)
df1.groupby(['tag_ids']).sum().plot(kind='pie', y='count', autopct='%1.0f%%',title='Popular Tags(categories) of books')

# From the pie chart we can easily observe the top 5 most popular categories book tags
# The error is for copy version of file