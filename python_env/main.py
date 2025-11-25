
import pandas as pd

df= pd.read_excel("read.xlsx")

df= df.dropna() # drop rows that has at least one missing value



print(df.to_string)

