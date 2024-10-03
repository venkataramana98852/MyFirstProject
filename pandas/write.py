import pandas as pd

df=pd.read_csv("data.csv")

print(pd.DataFrame(df))
df1=df.head(5)

maxpulse_column = df['Maxpulse'].sum()
print(maxpulse_column)
value = df.loc[2, 'Calories']
print(f'Value at row 2, column "Calories": {value}')

# df1.to_csv("output.csv", index= False)