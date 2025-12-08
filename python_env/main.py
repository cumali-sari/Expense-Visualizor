import pandas as pd
from categorize import*

df_raw = pd.read_excel("read.xlsx", header=None)

# drop rows that has at least one missing value
# by that get rid of lines before and after dataframe
df_raw= df_raw.dropna() 


# move header to df's columns

header_row = df_raw.apply(
    lambda row: row.astype(str).str.isalpha().any(),
    axis=1
).idxmax()

df = pd.read_excel("read.xlsx", header=header_row)

df= df.dropna()

df["Kategori"]= df["Açıklama"].apply(categorize_expense)

group = df.groupby("Kategori")


print(group["İşlem Tutarı"].sum())









