import pandas as pd
pd.set_option('display.max_colwidth', -1)
jeopardy_data=pd.read_csv('jeopardy.csv')

print(jeopardy_data.head())