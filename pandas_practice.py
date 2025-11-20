import pandas as pd

df = pd.DataFrame({
    'age': ['23', '45', '30'],
    'name': ['Tom', 'Jane', 'Alex']
})

print(df)

print(df.dtypes)
age = df["age"].astype(int)
print(age)