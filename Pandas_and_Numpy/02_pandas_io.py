import pandas as pd
data = {'Block': ['ALU', 'MEM'], 'Area': [1500, 8000]}
df = pd.DataFrame(data)

# Exporting data to CSV
csv_file = "area_report.csv"
df.to_csv(csv_file, index=False)
print(f"Exported successfully to {csv_file}")
