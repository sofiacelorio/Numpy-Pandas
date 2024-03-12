import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df)
rows= []
for i in range(df. shape [0]):
    if np.sum(df.iloc[i,:])>100:
        rows.append (i)
print(rows)