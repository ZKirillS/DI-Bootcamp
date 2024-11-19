-- PART 1

-- CREATE TABLE customer (
-- customer_id SERIAL,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL,
-- PRIMARY KEY (customer_id)
-- )

-- CREATE TABLE customer_profile (
-- profile_id INTEGER NOT NULL,
-- isLoggedIn BOOLEAN DEFAULT false,
-- PRIMARY KEY (profile_id),
-- CONSTRAINT fk_customer_id FOREIGN KEY (profile_id) REFERENCES customer (customer_id) ON DELETE CASCADE
-- )

-- INSERT INTO customer (first_name, last_name) 
-- VALUES ('John', 'Doe'),('Jerome', 'Lalu'),('Lea', 'Rive')

-- INSERT INTO customer_profile (profile_id)
-- VALUES (1),(2),(3)

-- SELECT * FROM customer_profile

-- INSERT INTO customer_profile (isLoggedIn, profile_id)
-- VALUES
-- (TRUE,(SELECT customer_id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')),
-- (FALSE,(SELECT customer_id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')),
-- (FALSE,(SELECT customer_id FROM customer WHERE first_name = 'Lea' AND last_name = 'Rive'))

-- SELECT customer.first_name
-- FROM customer
-- INNER JOIN customer_profile ON customer.customer_id = customer_profile.profile_id
-- WHERE customer_profile.isLoggedIn = TRUE

-- SELECT customer.first_name, COALESCE(customer_profile.isLoggedIn, FALSE) AS isLoggedIn
-- FROM customer
-- LEFT JOIN customer_profile ON customer.customer_id = customer_profile.profile_id

-- SELECT COUNT(*) AS num_not_logged_in
-- FROM customer 
-- LEFT JOIN customer_profile ON customer.customer_id = customer_profile.profile_id
-- WHERE customer_profile.isLoggedIn IS NULL OR customer_profile.isLoggedIn = FALSE;


-- PART 2
-- CREATE TABLE book (
-- book_id SERIAL PRIMARY KEY,
-- title VARCHAR(50) NOT NULL,
-- author VARCHAR(50) NOT NULL
-- )
-- SELECT * FROM book

-- INSERT INTO book (title, author)
-- VALUES ('Alice In Wonderland','Lewis Carroll'),
-- ('Harry Potter','J.K Rowling'),
-- ('To kill a mockingbird','Harper Lee')

-- CREATE TABLE student (
-- student_id SERIAL PRIMARY KEY,
-- name VARCHAR(50) NOT NULL UNIQUE,
-- age INT CHECK (age <= 15)
-- )

-- INSERT INTO student (name, age)
-- VALUES ('John',12),
-- ('Lera','11'),
-- ('Patrick','10'),
-- ('Bob',14)

-- CREATE TABLE library (
-- student_id INTEGER NOT NULL,
-- book_id INTEGER NOT NULL,
-- PRIMARY KEY (book_id, student_id),
-- FOREIGN KEY (book_id) REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- FOREIGN KEY (student_id) REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- borrowed_date DATE NOT NULL
-- )

-- INSERT INTO library (student_id,book_id,borrowed_date)
-- VALUES ((SELECT student_id FROM student WHERE name = 'John'),
-- (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
-- '15/02/2022')
-- INSERT INTO library (student_id,book_id,borrowed_date)
-- VALUES ((SELECT student_id FROM student WHERE name = 'Bob'),
-- (SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
-- '03/03/2021')
-- INSERT INTO library (student_id,book_id,borrowed_date)
-- VALUES ((SELECT student_id FROM student WHERE name = 'Lera'),
-- (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
-- '23/05/2021')
-- INSERT INTO library (student_id,book_id,borrowed_date)
-- VALUES ((SELECT student_id FROM student WHERE name = 'Bob'),
-- (SELECT book_id FROM book WHERE title = 'Harry Potter'),
-- '12/08/2021')

-- SELECT * FROM library

-- SELECT student.name, book.title
-- FROM library
-- INNER JOIN student ON library.student_id = student.student_id
-- INNER JOIN book ON book.book_id = library.book_id

-- SELECT AVG(student.age)
-- FROM library
-- INNER JOIN student ON library.student_id = student.student_id
-- INNER JOIN book ON book.book_id = library.book_id
-- WHERE book.title = 'Alice In Wonderland'

-- DELETE FROM student WHERE name = 'John';
-- SELECT * FROM library


