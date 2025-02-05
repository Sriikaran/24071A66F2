import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
}

df = pd.DataFrame(data)

df.to_csv('example.csv', index=False)

print("CSV file 'example.csv' created successfully.")

df = pd.read_csv('example.csv')

print(df.head())