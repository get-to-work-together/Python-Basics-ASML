import pandas as pd

pd.set_option('display.max_rows', 100)

filename = '../Sandbox/ca-500.csv'

df = pd.read_csv(filename, sep=';')

selection = df[['first_name','last_name','city']].query('city=="Montreal"')

cities = df['city'].value_counts()

print(df.columns)
print(selection)
print(cities)