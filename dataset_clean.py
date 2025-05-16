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
    vid = [] # list of all vids to help find video names
    rank = []
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
                if index[x] == "Video":
                    vid.append(ranklist[i])
                if index[x] == "rank":
                    rank.append(ranklist[i])
                if index[x] == "Category":
                    categories.append(ranklist[i])
                if index[x] == "Likes":
                    if int(a) == 0:
                        c += 1
                    else:
                        suml += int(a)
                    if int(a) > like[0]:
                        like[0] = int(a)
                        like[1] = df.iloc[rank[i]-1, 1]
                if index[x] == "Dislikes":
                    if int(a) == 0:
                        cc += 1
                    else:
                        sumd += int(a)
                    if int(a) > dislike[0]:
                        dislike[0] = int(a)
                        dislike[1] = df.iloc[rank[i]-1, 1]
                if index[x] == "Video views":
                    if int(a) == 0:
                        ccc += 1
                    else:
                        sumv += int(a)
                    if int(a) > view[0]:
                        view[0] = int(a)
                        view[1] = df.iloc[rank[i]-1, 1]


                i += 1
        x += 1
    cat = max(set(categories), key=categories.count) #this means that music videos are most likely to be trending
    cat1 = categories.count(cat)
    md = sumd / l #mean of dislikes, likes, and views
    ml = suml / l
    mv = sumv / l
    print("Here is the top category out of all 1000 videos, and the amount of videos with that category")
    print(cat)
    print(cat1)
    print("here are the average of the views, likes, and dislikes")
    print(str(int(mv))+" , "+str(int(ml))+" , "+str(int(md)))
    print("here are the videos with the highest views,likes, and dislikes in that order")
    print(view[1]+"\nViews: "+str(view[0])+"\n")
    print(like[1]+"\nLikes: "+str(like[1])+"\n")
    print(dislike[1]+"\nDislikes: "+str(dislike[0]))
process(df)
