import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS orderentries (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")

# Insert sample data
cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (111, 'Alice', 'alice@example.com')")
cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (222, 'Bob', 'bob@example.com')")
cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (333, 'jack', 'jack@example.com')")
cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (444, 'mike', 'mike@example.com')")

cursor.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (211, 'apple watch', 199.99)")
cursor.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (212, 'iphone', 729.99)")
cursor.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (213, 'Samsung phone', 559.99)")
cursor.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (214, 'smart watch', 195.99)")
cursor.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (215, 'ipods', 99.99)")
cursor.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (216, 'wireless headset', 229.99)")

cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (311, 111, '2024-06-03')")
cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (312, 111, '2025-05-03')")
cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (313, 111, '2025-05-03')")
cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (314, 111, '2025-06-03')")
cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (315, 222, '2025-04-03')")
cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (316, 222, '2024-04-03')")
cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (317, 333, '2025-02-03')")
cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, order_date) VALUES (318, 444, '2024-02-03')")

cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (1, 311, 211, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (2, 311, 212, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (3, 311, 215, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (4, 311, 216, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (5, 312, 213, 4)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (21, 312, 214, 4)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (6, 313, 213, 6)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (7, 313, 214, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (8, 313, 215, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (9, 314, 215, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (10, 314, 211, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (11, 314, 212, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (12, 314, 213, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (13, 315, 213, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (14, 315, 214, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (15, 316, 215, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (16, 316, 216, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (17, 317, 211, 2)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (18, 317, 212, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (19, 318, 213, 1)")
cursor.execute("INSERT OR IGNORE INTO orderentries (id, order_id, product_id, quantity) VALUES (20, 318, 214, 1)")



conn.commit()
conn.close()
