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
    #to clean - video, category
    #to analyze - views, likes, dislikes, category, and publish
    ranklist = df["Likes"].values.tolist()
    l = len(ranklist)
    i = 0
    sum1 = 0
    miss = 0
    print(l)
    for i in range(0,l):
        a = str(ranklist[i])
        a = a.replace(",","")
        if a == "nan":
            #print(ranklist[i])
            ranklist.insert(i,"Miss")
            miss += 1
            #print(ranklist[i])
            #print(" ")
        else:
            ranklist.insert(i,a)
            sum1 += int(a)
        i += 1
    df['Likes'] = pd.Series(ranklist) 
    #print("This is the mean amount of likes across all videos:")
    print(ranklist)
    print(df)
    #print(sum1)
process(df)

#idx.str.rstrip()
#Out[31]: Index([' jack', 'jill', ' jesse', 'frank'], dtype='object')

#func search/sort?
#mean / median / mode / standard deviation  
#value of views / likes / dislikes / date published
