import pandas as pd

df = pd.read_csv("people.csv")

# print(df)

# print(df.to_string())

df = pd.read_json("pokemon.json")

print(df)