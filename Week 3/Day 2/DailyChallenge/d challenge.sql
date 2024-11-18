-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- it will create a new table with id and name columns


-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

--inserting new data

-- SELECT * FROM FirstTab

--output all the data from the table

-- CREATE TABLE SecondTab (
--     id integer 
-- )

--creating second table

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)

-- SELECT * FROM SecondTab

-- QUSTIONS
-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- we are picking id null from table 2 and looking all id from table 1 not in selected id's from table 2

-- SELECT COUNT(*) 
--  FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- we can see how much repetitive id 5 from tables exists

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- how much repetitive id's tab 1 and tab 2 

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- how much id's from tab 1 repetative in tab 2, but not null id's










