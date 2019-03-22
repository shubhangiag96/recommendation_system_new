import pandas as pd
import numpy as np
import json
with open('business.json') as j_file:
    jdata = json.load(j_file)
df11 = pd.DataFrame(jdata)
df22 = pd.DataFrame(np.random.randint(3000,10000,size=(174568, 1)), columns=list('c'))
print(df22.head())
df3=df11.join(df22)
print(df3.head())
with open('cost_rest.json', 'w') as f:
    f.write(df3.to_json(orient='records', lines=True))
