#!/usr/bin/python

import pandas as pd

filename = 'ca-500.csv'

df = pd.read_csv(filename, sep = ';')

df_selected = df.query('city=="Montreal"')

print(df_selected[['first_name', 'last_name', 'city']])

counts = df.value_counts(['city'])
print(counts)