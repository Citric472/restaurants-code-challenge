import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('restaurant_reviews.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price INTEGER
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                restaurant_id INTEGER,
                customer_id INTEGER,
                star_rating INTEGER,
                FOREIGN KEY(restaurant_id) REFERENCES restaurants(id),
                FOREIGN KEY(customer_id) REFERENCES customers(id)
            )''')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
