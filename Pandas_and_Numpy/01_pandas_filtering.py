import pandas as pd
data = {'Test': ['t1', 't2', 't3'], 'Errors': [0, 15, 0], 'Time': [1.2, 5.5, 0.9]}
df = pd.DataFrame(data)

# Filtering for failing tests
failed = df[df['Errors'] > 0]
print("Failed Tests Only:\n", failed)

# Adding a new calculated column
df['Slow'] = df['Time'] > 2.0
print("\nDataFrame with 'Slow' flag:\n", df)
