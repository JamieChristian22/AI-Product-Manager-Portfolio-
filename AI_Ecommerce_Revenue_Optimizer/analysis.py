import pandas as pd

df = pd.read_csv('dataset.csv')
print('Conversion Rate:', df['conversion'].mean())
print('Average Session:', df['session_length'].mean())
print('Total Revenue:', df['revenue'].sum())
