medicine_catalog = """
    CREATE TABLE medicines (
        id INT AUTO_INCREMENT PRIMARY KEY,
        medicine VARCHAR(100) NOT NULL UNIQUE,
        expiry DATE NOT NULL,
        quantity INT NOT NULL DEFAULT 0,
        price DECIMAL(5, 2)
    )
"""

customer_info = """
    CREATE TABLE customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        phone INT(10) NOT NULL UNIQUE
    )
"""

purchase_record = """
    CREATE TABLE purchase_records (
        id INT AUTO_INCREMENT PRIMARY KEY,
        medicine_id INT NOT NULL,
        customer_id INT NOT NULL
    )
"""