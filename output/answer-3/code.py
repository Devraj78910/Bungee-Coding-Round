import pandas as pd
	
df = pd.read_csv("input\question-3\main.csv")

df1 = df[['Team','Yellow Cards','Red Cards']]

df2 = df1.sort_values(["Red Cards", "Yellow Cards"], ascending = (False, False))

df2.to_csv('output\\answer-3\\main.csv', index=False)