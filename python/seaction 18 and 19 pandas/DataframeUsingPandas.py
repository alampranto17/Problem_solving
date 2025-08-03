import numpy as np
import pandas as pd

#using list making data frame 

# student_data=[
#     [100,80,10],
#     [60,70,7],
#     [120,100,14],
#     [80,50,2]
# ]

# columns=['Id','Marks','packages']

# # print(student_data)

# data=pd.DataFrame(student_data,columns=columns)

# print(data)

# print(type(data))

# print(type(data.Id))

# #dic use kore dataframe

# student_dic={
#     'iq':[100,90,120,80],
#     'marks':[80,70,100,50],
#     'package':[10,7,14,2]
# }

# print(pd.DataFrame(student_dic))

#using read_CSV

data_movie=pd.read_csv('D:\Problem solving\Problem_solving\python\All Datasets\movies.csv')
# print(data_movie)

# print(data_movie.describe())

# another dataset

IPL_Matches=pd.read_csv('D:\Problem solving\Problem_solving\python\All Datasets\ipl-matches.csv')

# print(IPL_Matches)

# dataFrame attributes and methods

# --------------shape --> show row and column number

# print("movie dataset colums and rows : ",data_movie.shape)

#dtype--- showing all the columns data type 

print(IPL_Matches.dtypes)



