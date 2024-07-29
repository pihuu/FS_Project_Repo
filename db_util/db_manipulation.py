import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('financial_data.db')
cursor = conn.cursor()

# Fetch the data
cursor.execute('SELECT * FROM financial_data')
rows = cursor.fetchall()

# Close the connection
conn.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(rows, columns=['id', 'date', 'description', 'amount', 'category'])

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Manipulations
# Calculate total income
total_income = df[df['category'] == 'Income']['amount'].sum()
print("\nTotal Income:", total_income)

# Calculate total expenses
total_expenses = df[df['category'] == 'Expense']['amount'].sum()
print("Total Expenses:", total_expenses)

# Calculate net balance
net_balance = total_income + total_expenses  # Expenses are negative
print("Net Balance:", net_balance)

# Filter data for a specific category
income_df = df[df['category'] == 'Income']
print("\nIncome DataFrame:")
print(income_df)

# Add a new column 'balance' which is cumulative sum of 'amount'
df['balance'] = df['amount'].cumsum()
print("\nDataFrame with Balance Column:")
print(df)
