CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

-- ALTER TABLE Customers 
-- 	ALTER COLUMN city TYPE VARCHAR(50);

-- Insert data into the table
INSERT INTO Customers 
	(customer_id, customer_name, city)
VALUES
    (1, 'John Doe', 'NYC'),
    (2, 'Jane Smith', 'LA'),
    (3, 'David Johnson', 'Chg');

-- Create the campus table
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
	customer_id INTEGER,
	FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount FLOAT
);

-- Insert data into the campus table
INSERT INTO Orders (order_id, customer_id, order_date, total_amount)
VALUES
    (1, 1, '2022-01-10', 100.00),
    (2, 1, '2022-02-15', 150.00),
    (3, 2, '2022-03-20', 200.00),
    (4, 3, '2022-04-25', 50.00);
	