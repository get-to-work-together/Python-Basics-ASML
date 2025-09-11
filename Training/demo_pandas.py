import pandas as pd


df = pd.DataFrame([
    {'id': '1', 'first_name': 'Peter', 'last_name':'Anema', 'residence': 'Lhee'},
    {'id': '2', 'first_name': 'Jan', 'last_name':'Boersma', 'residence': 'Eindhoven'},
    {'id': '3', 'first_name': 'Sandra', 'last_name':'Jans', 'residence': 'Amsterdam'},
])

df['name'] = df['first_name'] + ' ' + df['last_name']

print(df)

print(df.query('residence=="Eindhoven"'))
