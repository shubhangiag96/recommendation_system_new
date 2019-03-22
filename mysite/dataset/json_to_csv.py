import pandas as pd

df = pd.read_json('cost_rest.json.json')


print(df.head())

df.to_csv('cost_rest.json.csv')