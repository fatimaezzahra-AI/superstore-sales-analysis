import pandas as pd
import sqlite3

# 1. Load the dataset from CSV (or Excel as fallback)
try:
    df = pd.read_csv('Superstore.csv', encoding='latin1')
    print("Dataset loaded successfully from CSV file.")
except Exception as e:
    df = pd.read_excel('Superstore.xlsx')
    print("Dataset loaded successfully from Excel file.")

# 2. Connect to SQLite database (creates 'superstore.db' if it doesn't exist)
conn = sqlite3.connect('superstore.db')

# 3. Export the dataframe into an SQL table named 'sales'
df.to_sql('sales', conn, if_exists='replace', index=False)

print("Data successfully converted and stored in 'superstore.db'!")

# 4. Close the database connection
conn.close()