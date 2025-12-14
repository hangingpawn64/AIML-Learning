import pandas as pd

print(pd.__version__)

# Series = It is a pandas 1D array that can hold any data type.
#          Like a single column in a spreadsheet

data = [100, 102.2, 104.6, 200, 202]

series = pd.Series(data)

#print(series)  # 0 100
               # 1 102
               # 2 104
               # dtype: float64
               # strings will come as dtype: objects,
               # boolean as dtype: bool

series1 = pd.Series(data, index=["a", "b", "c", "d", "e"])
# print(series1)
# print(series1.loc["a"]) # 100

series1.loc["c"] = 200
# print(series1)
# print(series1.iloc[2])

# print(series[series >= 200])

calories = {"Day 1": 1750,
            "Day 2": 3510,
            "Day 3": 1700
            }

series = pd.Series(calories)

print(series)

series.loc["Day 3"] += 500;

print(series)

print(series[series >= 2000])

# Exercise
pokemons = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard"]

series2 = pd.Series(pokemons, index=[1,2,3,4,5,6])
print(series2)
