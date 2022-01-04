import pandas as pd
std=pd.read_csv("pandas/IPL_matches (1).csv")
print(std[std['season']==2008])