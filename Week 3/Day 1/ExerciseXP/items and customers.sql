-- CREATE TABLE items (
-- item_id SERIAL PRIMARY KEY,
-- item_name VARCHAR (100) NOT NULL,
-- item_price INT NOT NULL
-- )

-- CREATE TABLE customers (
-- customer_id SERIAL PRIMARY KEY,
-- customer_name VARCHAR (50) NOT NULL,
-- customer_lastname VARCHAR (100) NOT NULL
-- )

-- INSERT INTO items (item_name,item_price) VALUES
-- ('Small Desk',100),
-- ('Large Desk',300),
-- ('Fan',80);
-- SELECT * FROM items
-- SELECT item_name FROM items WHERE item_price > 80
-- SELECT item_name FROM items WHERE item_price <= 300



-- INSERT INTO customers (customer_name,customer_lastname) VALUES 
-- ('Greg','Jones'),
-- ('Sandra','Jones'),
-- ('Scott ','Scott '), --i have here a space so i need to TRIM when SELECT
-- ('Trevor','Green'),
-- ('Melanie','Johnson');

-- SELECT * FROM customers
-- SELECT customer_name FROM customers WHERE customer_lastname = 'Smith' 
-- SELECT customer_name FROM customers WHERE customer_lastname = 'Jones'
-- SELECT * FROM customers WHERE TRIM(customer_name) != 'Scott'
