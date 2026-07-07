-- =====================================
-- Sample Customers
-- =====================================

INSERT INTO Customers VALUES
(1, 'Alice Johnson', 'Seattle', 'Washington', 'USA', 'Consumer'),
(2, 'Bob Smith', 'Bellevue', 'Washington', 'USA', 'Corporate'),
(3, 'Charlie Brown', 'Portland', 'Oregon', 'USA', 'Home Office'),
(4, 'David Lee', 'San Francisco', 'California', 'USA', 'Consumer'),
(5, 'Emma Davis', 'Los Angeles', 'California', 'USA', 'Corporate');

-- =====================================
-- Sample Products
-- =====================================

INSERT INTO Products VALUES
(101, 'Laptop', 'Technology', 'Computers', 1200),
(102, 'Monitor', 'Technology', 'Accessories', 300),
(103, 'Office Chair', 'Furniture', 'Chairs', 250),
(104, 'Desk', 'Furniture', 'Tables', 450),
(105, 'Printer', 'Technology', 'Printers', 500);

-- =====================================
-- Sample Orders
-- =====================================

INSERT INTO Orders VALUES
(1001, 1, '2026-01-10', 'Delivered'),
(1002, 2, '2026-01-15', 'Delivered'),
(1003, 3, '2026-02-05', 'Delivered'),
(1004, 4, '2026-02-20', 'Cancelled'),
(1005, 5, '2026-03-01', 'Delivered');

-- =====================================
-- Sample Sales
-- =====================================

INSERT INTO Sales VALUES
(1,1001,101,2,2400,600,0.05),
(2,1002,103,4,1000,250,0.10),
(3,1003,104,1,450,120,0.00),
(4,1005,102,3,900,220,0.15),
(5,1005,105,1,500,100,0.05);