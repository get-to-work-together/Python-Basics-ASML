import pandas as pd

filename = 'emails.txt'

df = pd.read_csv(filename, skipinitialspace=True)

print(type(df))
print(df.columns)

df_selected = df[df['EMAIL'].str.endswith('@asml.com')]
print(df_selected)