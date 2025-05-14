import pandas as pd
import numpy as np
data_str = "/workspaces/electricvehicle_databasics/top-1000-trending-youtube-videos copy.csv"
index =["rank","Video","Video views","Likes","Dislikes","Category","published"]
df = pd.read_csv(data_str)

def process(df): #search through and analise the data
    index =["rank","Video","Video views","Likes","Dislikes","Category","published"]
    ll = len(index)
    i = 0
    x = 0
    like = [0,0]
    dislike = [0,0]
    view = [0,0]
    suml = 0
    sumd = 0
    sumv = 0
    miss = 0
    categories = []
    for x in range(0,ll):
        indexlist = ["rank","Video views","Likes","Dislikes","published"] #use this to determine if this value needs to be int or str.
        ranklist = df[index[x]].values.tolist()
        l = len(ranklist)
        for i in range(0,l):
            a = str(ranklist[i])
            a = a.replace(",","")
            #if index[x] in indexlist:
            #    a = int(ranklist[i])
            #else:
            #    a = str(ranklist[i])
            if a == "nan":
                if index[x] == "Video":
                    df.remove(i)
                    l = l - 1 
                if index[x] == "Video views":
                    ranklist[i:i+1] = [0]
                miss += 1
                i += 1
                if index[x] == "Likes":
                    ranklist[i:i+1] = [0]
                if index[x] == "Dislikes":
                    ranklist[i:i+1] = [0]
                if index[x] == "published":
                    ranklist[i:i+1] = [0]
            else:
                if index[x] == "rank":
                    rank = ranklist[i]
                if index[x] == "Category":
                    categories.append(ranklist[i])
                if index[x] == "Likes": #Sort and make data here
                    suml += int(a)
                    if int(a) > like[0]:
                        like = [int(a),df.loc[int(rank)-1]]
                if index[x] == "Dislikes":
                    sumd += int(a)
                    if int(a) > dislike[0]:
                        dislike = [int(a),df.loc[int(rank)-1]]
                if index[x] == "Video views":
                    sumv += int(a)
                    if int(a) > view[0]:
                        view = [int(a),df.loc[int(rank)-1]]

                i += 1
        x += 1
    md = sumd / l
    ml = suml / l
    mv = sumv / 1
    print(mv)
    print(ml)
    print(md)
    print(df.loc[5])
    print(view)
process(df)
