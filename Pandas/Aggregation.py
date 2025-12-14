import pandas as pd

# Aggregate Funtions = Reduces a set of values into a single summary value
#                      Used to summarize and analyse data
#                      Often used with the groupby() function

df = pd.read_csv("pokemon.csv")

# Whole DataFrame
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Single Column
# print(df["HP"].mean())
# print(df["HP"].sum(numeric_only=True))
# print(df["HP"].min(numeric_only=True))
# print(df["HP"].max(numeric_only=True))
# print(df["HP"].count())

group = df.groupby("Type 1")

# print(group["HP"].mean())
# print(group["HP"].min())
# print(group["HP"].max())
# print(group["HP"].count())