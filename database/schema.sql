-- =====================================
-- BI Navigator Retail Database Schema
-- =====================================

DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city TEXT,
    state TEXT,
    country TEXT,
    segment TEXT
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    subcategory TEXT,
    unit_price REAL
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    order_status TEXT,
    FOREIGN KEY(customer_id)
        REFERENCES Customers(customer_id)
);

CREATE TABLE Sales (
    sale_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    revenue REAL,
    profit REAL,
    discount REAL,
    FOREIGN KEY(order_id)
        REFERENCES Orders(order_id),
    FOREIGN KEY(product_id)
        REFERENCES Products(product_id)
);