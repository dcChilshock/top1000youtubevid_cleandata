import pandas as pd
import numpy as np
data_str = "/workspaces/electricvehicle_databasics/top-1000-trending-youtube-videos copy.csv"
index =["rank","Video","Video views","Likes","Dislikes","Category","published"]
df = pd.read_csv(data_str)
#length = 6
#for i in
#search through and handle missing values
#value_list = df[1:2].values.tolist() #IMPORTANT
#print(value_list)
#print(df.loc[df["rank"]> 50])\
#print(df["rank"])

def process(df): #search through and analise the data
    ranklist = df["Likes"].values.tolist()
    #print(ranklist)
    l = len(ranklist)
    i = 0
    sum1 = 0
    for i in range(0,l):
        a = int(ranklist[i].strip(","))
        sum1 += int(ranklist[i])
    print(str(sum1))
    
process(df)

#idx.str.rstrip()
#Out[31]: Index([' jack', 'jill', ' jesse', 'frank'], dtype='object')

#func search/sort?
#mean / median / mode / standard deviation  
#value of views / likes / dislikes / date published
