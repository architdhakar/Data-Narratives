import numpy as np
import pandas as pd
import scipy
from matplotlib import pyplot as plt
#Question 1: TO visualise that for a given author, chances that he will write a book with very good ratings on the basis of previous ratings on his books.
file_path1='https://github.com/zygmuntz/goodbooks-10k/blob/master/books.csv?raw=true'
df=pd.read_csv(file_path1)       # To open the csv file
y=df["authors"].value_counts()["Suzanne Collins"]               # To find the number books written by given author
x=df.query('authors=="Suzanne Collins"')['average_rating']      # To find the average rating on diffrent books
print("Number books written by Suzanne Collins",y)
print("book_id  average_rating ")
print(x)

#Another example
m=df["authors"].value_counts()["Douglas Adams"]               # To find the number books written by given author
z=df.query('authors=="Douglas Adams"')['average_rating']      # To find the average rating on diffrent books
print("Number books written by Douglas Adams are",m)
print("book_id  average_rating ")
print(z)
data={"Suzanne Collins":[4.34,4.30,4.03,4.49,3.99,4.25,4.20,4.17,4.21],"Douglas Adams":[4.20,4.37,4.22,4.19,4.08,3.97,3.96,4.51,3.92]}
df1=pd.DataFrame(data)
df1.plot.kde()