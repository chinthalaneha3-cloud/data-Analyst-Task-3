import sqlite3

con = sqlite3.connect("shop.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE orders(
id INTEGER,
name TEXT,
product TEXT,
amount INTEGER
)
""")

# Insert data
data = [
    (1, "Neha", "Laptop", 50000),
    (2, "Anu", "Mobile", 20000),
    (3, "Ravi", "Mouse", 1000),
    (4, "Priya", "Laptop", 55000)
]

cur.executemany("INSERT INTO orders VALUES(?,?,?,?)", data)

# SELECT and WHERE
print("Orders above 10000:")
cur.execute("SELECT * FROM orders WHERE amount > 10000")
print(cur.fetchall())

# ORDER BY
print("\nOrders by amount:")
cur.execute("SELECT name, amount FROM orders ORDER BY amount DESC")
print(cur.fetchall())

# SUM
print("\nTotal sales:")
cur.execute("SELECT SUM(amount) FROM orders")
print(cur.fetchone())

# AVG
print("\nAverage sales:")
cur.execute("SELECT AVG(amount) FROM orders")
print(cur.fetchone())

con.commit()
con.close()

import sqlite3

con = sqlite3.connect("shop.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE orders(
id INTEGER,
name TEXT,
product TEXT,
amount INTEGER
)
""")

# Insert data
data = [
    (1, "Neha", "Laptop", 50000),
    (2, "Anu", "Mobile", 20000),
    (3, "Ravi", "Mouse", 1000),
    (4, "Priya", "Laptop", 55000)
]

cur.executemany("INSERT INTO orders VALUES(?,?,?,?)", data)

# SELECT and WHERE
print("Orders above 10000:")
cur.execute("SELECT * FROM orders WHERE amount > 10000")
print(cur.fetchall())

# ORDER BY
print("\nOrders by amount:")
cur.execute("SELECT name, amount FROM orders ORDER BY amount DESC")
print(cur.fetchall())

# SUM
print("\nTotal sales:")
cur.execute("SELECT SUM(amount) FROM orders")
print(cur.fetchone())

# AVG
print("\nAverage sales:")
cur.execute("SELECT AVG(amount) FROM orders")
print(cur.fetchone())

con.commit()
con.close()

print("\nTask completed successfully!")