import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy as sp
#Question3
print("Ans1.")
file_path1='https://github.com/zygmuntz/goodbooks-10k/blob/master/books.csv?raw=true'
df=pd.read_csv(file_path1) #To open the csv file
df1=df[["original_title","average_rating"]]    #To access the title and rating column
sorted=df1.sort_values(by='average_rating')    #To sort the rating in accending order

df2=sorted.tail(10)                            # To access the best rating books
print("1.Best rating books")
print(df2)
print("")
print("")
print("2.Books with higher 1 rating")
# From this data we can recommend the user to read these books which are liked by most of the users
df3=df[["original_title","ratings_1"]]
sorted=df3.sort_values(by=["ratings_1"])    #To sort the rating in accending order
df4=sorted.tail(10)
print(df4)
print('')
print('')

print("3.Most readed Book/Books with higher rating count")

df5=df[["original_title","average_rating","ratings_count"]]
sorted=df5.sort_values(by=["ratings_count"])    #To sort the rating in accending order
df6=sorted.tail(5)
print(df6)


# From this data we can observe that a juding a book by its average_rate is not the good parameter because if no. of users who 
# has given ratings are few in case of best rating books where averages decreases when more no of users have given the ratings. 
