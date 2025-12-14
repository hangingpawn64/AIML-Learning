import pandas as pd

df = pd.read_csv("people.csv", index_col="First Name")
# print(df["Job Title"].to_string())

# print(df[["First Name","Last Name", "Sex"]].to_string())

# SELECTION BY ROWS

print(df.loc["Shelby", ["Last Name", "Sex"]])