import pandas as pd
import numpy as np
data_str = "/workspaces/electricvehicle_databasics/top-1000-trending-youtube-videos copy.csv"
index =["rank","Video","Video views","Likes","Dislikes","Category","published"]
df = pd.read_csv(data_str)
#value_list = df[1:2].values.tolist() #IMPORTANT
#print(value_list)
#print(df.loc[df["rank"]> 50])\
#print(df["rank"])

def process(df): #search through and analise the data
    index =["rank","Video","Video views","Likes","Dislikes","Category","published"]
    ll = len(index)
    #to clean - all
    #to analyze - views, likes, dislikes, category, and publish
    i = 0
    x = 0
    like = 0
    sum1 = 0
    miss = 0
    for x in range(0,ll):
        ranklist = df[index[x]].values.tolist()
        l = len(ranklist)
        for i in range(0,l):
            a = str(ranklist[i])
            a = a.replace(",","")
            if a == "nan":
                if index[x] == "Video":
                    df.remove(i)
                    l -= 1 
                ranklist[i:i+1] = ["Miss"]  #Handle missing values here, and clean data set
                miss += 1
                i += 1
            else:
                if index[x] == "Likes":
                    u = int(a)
                    if int(u) > like:
                        like = int(u)
                if index[x] == "Views":
                    sum1 += int(a) #here sort the data set?
                i += 1
        x += 1
    print(like)
    #lenn = len(ranklist)
    #print(str(lenn))
    #df['Likes'] = pd.Series(ranklist) 
    #print("This is the mean amount of likes across all videos:")
    #print(ranklist)
    #print(df)
    #print(sum1)
process(df)

#idx.str.rstrip()
#Out[31]: Index([' jack', 'jill', ' jesse', 'frank'], dtype='object')

#func search/sort?
#mean / median / mode / standard deviation  
#value of views / likes / dislikes / date published
