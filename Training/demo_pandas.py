import pandas as pd


df = pd.read_csv('data.csv')

df = pd.read_csv('data.csv', sep=';', dayfirst=True, decimal=',')