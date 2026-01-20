import pandas as pd

df = pd.read_csv('../Sandbox/ca-500.csv',
                 sep=';',
                 decimal=',',
                 dayfirst=True)

print(df.info())