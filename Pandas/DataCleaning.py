import pandas as pd

# Data Cleaning = the process of fixing/removing
#                 incomplete,incorrect, or irrelevant data.
#                 ~75% of work done with pandas is data cleaning

df = pd.read_csv("pokemon.csv")

# 1. Drop irrelevant data
# df = df.drop(columns=["Legendary", "Type 2", "#"])

# 2. Handle Missing Data
# df = df.dropna(subset=["Type 2"]) ## this will drop rows which do not have a type 2
# df = df.fillna({"Type 2": "None"}).to_string()

# 3. Fix inconsitstent values
df["Type1"] = df["Type 1"].replace({"Grass" : "GRASS",
                                   "Fire": "FIRE",
                                   "Water" : "WATER"})

# 4. Standardize text
df["Name"] = df["Name"].str.lower()

# 5. Fix data Types
df["Legendary"] = df["Legendary"].astype(int)

# 6. Remove Duplicates
df = df.drop_duplicates()
print(df)