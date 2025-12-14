import pandas as pd

data = {"Name": ["Shinchan", "Kazama", "Masao"],
        "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index= ["Child1", "Child2", "Child3"])

# print(df)

# print(df.loc["Child1"])

# print(df.iloc[0])

## Add a new Column

df["Job"] = ["Cook", "N/A", "Cashier"]

# print(df)

## Add a new Row

new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}],
                        index=["Child4"])
df = pd.concat([df, new_row])

new_rows = pd.DataFrame([{"Name": "Bochan", "Age": 14, "Job": "Collector"},
                         {"Name": "Nany", "Age": 25, "Job": "Fashion Designer"},
                         {"Name": "Shiro", "Age": 18, "Job": "Gaurd"}],
                         index=["Child5", "Child6", "Child7"])
df = pd.concat([df, new_rows])

print(df)