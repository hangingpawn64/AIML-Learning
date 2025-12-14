import pandas as pd

df = pd.read_csv("pokemon.csv")

#FILTERING : Keeping the rows that match a condition

Legendary_pokemon = df[df["Legendary"] == True]
FireFlying_Pokemon = df[(df["Type 1"] == "Fire") & 
                    (df["Type 2"] == "Flying")]

print(FireFlying_Pokemon)

