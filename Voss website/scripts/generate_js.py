import pandas as pd

# Adjust this path if your Excel lives elsewhere:
df = pd.read_excel('catalog-2025-05-27-1526.xlsx', header=1)

items = df[['Item Name', 'Price']].dropna(subset=['Item Name'])

for _, row in items.iterrows():
    name  = row['Item Name'].replace('"','\\"').strip()
    price = f"${float(row['Price']):.2f}"
    print("        {")
    print(f"          name: \"{name}\",")
    print(f"          img: \"\",  # ← add your image URL here")
    print(f"          price: \"{price}\",")
    print(f"          description: \"<p>No additional details available.</p>\",")
    print("        },")
