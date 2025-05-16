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
    c = 0
    cc = 0
    ccc = 0
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
                    pass 
                    ranklist[i:i+1] = [0]
                miss += 1
                i += 1
                if index[x] == "Likes":
                    pass
                    ranklist[i:i+1] = [0]
                if index[x] == "Dislikes":
                    pass
                    ranklist[i:i+1] = [0]
                if index[x] == "published":
                    pass
                    ranklist[i:i+1] = [0]
                if index[x] == "Category":
                    pass
                    ranklist[i:i+1] = ["na"]
            else:
                if index[x] == "rank":
                    rank = ranklist[i]
                if index[x] == "Category":
                    categories.append(ranklist[i])
                if index[x] == "Likes": #Sort and make data here
                    if int(a) == 0:
                        c += 1
                    else:
                        suml += int(a)
                    if int(a) > like[0]:
                        like = [int(a),df.loc[int(rank)+1]]
                if index[x] == "Dislikes":
                    if int(a) == 0:
                        cc += 1
                    else:
                        sumd += int(a)
                    if int(a) > dislike[0]:
                        dislike = [int(a),df.loc[int(rank)=1]]
                if index[x] == "Video views":
                    if int(a) == 0:
                        ccc += 1
                    else:
                        sumv += int(a)
                    if int(a) > view[0]:
                        view = [int(a),df.loc[int(rank)]]

                i += 1
        x += 1
    cat = max(set(categories), key=categories.count) #this means that music videos are most likely to be trending
    cat1 = categories.count(cat)
    md = sumd / l #mean of dislikes, likes, and views
    ml = suml / l
    mv = sumv / 1

    #print("Here is the top category out of all 1000 videos, and the amount of videos")
    #print(cat1)
    #print(cat)
    #print("here are the means of the views, likes, and dislikes")
    #print(mv)
    #print(ml)
    #print(md)
    #print("here are the videos with the highest views,likes, and dislikes in that order")
    #print(view[0])
    #print(view[1])
    #print(like[0])
    #print(like[1])
    #print(dislike[0])
    #print(dislike[1])
process(df)
