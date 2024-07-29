import sqlite3

# Step 1: Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('financial_data.db')
cursor = conn.cursor()

# Step 2: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS financial_data (
    id INTEGER PRIMARY KEY,
    date TEXT,
    description TEXT,
    amount REAL,
    category TEXT
)
''')

# Step 3: Insert some sample data
sample_data = [
    ('2023-01-01', 'Salary', 3000, 'Income'),
    ('2023-01-15', 'Groceries', -150, 'Expense'),
    ('2023-01-20', 'Electricity Bill', -75, 'Expense'),
    ('2023-01-25', 'Freelance Project', 500, 'Income')
]

cursor.executemany('''
INSERT INTO financial_data (date, description, amount, category)
VALUES (?, ?, ?, ?)
''', sample_data)

# Commit the transaction
conn.commit()

# Step 4: Fetch the data
cursor.execute('SELECT * FROM financial_data')
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(row)

# Close the connection
conn.close()
