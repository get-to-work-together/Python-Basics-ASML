import pandas as pd

#%%
filename = r'/Users/peter/Computrain/_InCompany/ASML/Python Basics/Sandbox/ca-500.csv'
df = pd.read_csv(filename, sep=';')

#%%
print(df.info())

print(df[['first_name', 'last_name']].head(20))
