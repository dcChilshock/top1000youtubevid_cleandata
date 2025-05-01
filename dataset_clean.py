import pandas as pd
import numpy as np
data_str = "/workspaces/electricvehicle_databasics/top-1000-trending-youtube-videos copy.csv"
pd.read_csv(data_str,index=["rank","Video","Video views","Likes","Dislikes","Category","published"])
#search through and handle missing values