import pandas as pd

df=pd.read_json("restaurant.json")
df.to_csv('restaurant.csv')