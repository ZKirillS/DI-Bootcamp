-- EXERCISE 1
-- 1

-- SELECT name FROM language

-- 2 

-- SELECT film.title, film.description, language.name
-- FROM film
-- INNER JOIN language ON language.language_id = film.language_id
-- ORDER BY film.title ASC

-- 3

-- SELECT film.title, film.description, language.name
-- FROM film
-- FULL JOIN language ON language.language_id = film.language_id
-- WHERE film.title IS NULL or film.title IS NOT NULL
-- ORDER BY language.name ASC

-- 4

-- CREATE TABLE new_film(
-- new_film_id SERIAL PRIMARY KEY,
-- new_film_name VARCHAR(100) NOT NULL
-- )
-- INSERT INTO new_film (new_film_name)
-- VALUES ('STAR WARS'),
-- ('Lord of the rings'),
-- ('Hobbit')
-- SELECT * FROM new_film

-- 5

-- CREATE TABLE customer_review(
-- review_id SERIAL PRIMARY KEY,
-- film_id INTEGER REFERENCES new_film (new_film_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- language_id INTEGER REFERENCES language (language_id),
-- title VARCHAR(50),
-- score INT CHECK (score BETWEEN 1 AND 10),
-- review_text TEXT NOT NULL,
-- last_update DATE NOT NULL
-- )
-- SELECT * FROM customer_review

-- 6

-- INSERT INTO customer_review (film_id, language_id, title,
-- score, review_text,last_update)
-- VALUES (1,
-- (SELECT language_id FROM language WHERE name = 'English'),
-- 'STAR WARS GREATEST REVIEW',
-- 10,
-- 'I enjoyed the story and battles. I saw all 9 parts and it was great!',
-- CURRENT_DATE);

-- SELECT new_film.new_film_name, customer_review.title, customer_review.score
-- FROM new_film
-- INNER JOIN customer_review ON customer_review.film_id = new_film.new_film_id

-- INSERT INTO customer_review (film_id, language_id, title,
-- score, review_text,last_update)
-- VALUES (3,
-- (SELECT language_id FROM language WHERE name = 'English'),
-- 'Hobbit iss a great movie',
-- 9,
-- 'I enjoyed the story and battles. I saw all 3 parts and it was awesome!',
-- CURRENT_DATE);

-- 7

-- DELETE FROM new_film WHERE new_film_name = 'Hobbit'
-- SELECT * FROM customer_review




-- EXERCISE 2

-- 1
-- UPDATE customer_review
-- SET language_id = (SELECT language_id FROM language WHERE name = 'Japanese')
-- WHERE film_id = 1

-- SELECT * FROM customer_review

-- 2
-- defined keys are store_id, address_id, u should make reference to this keys to add new customer

-- 3
-- DROP TABLE customer_review
-- SELECT * FROM customer_review
-- it was easy step, table was just deleted

-- 4
-- SELECT rental_id, return_date
-- FROM rental
-- WHERE return_date IS NULL

-- 5
-- SELECT rental.rental_id, rental.return_date, payment.amount
-- FROM rental
-- INNER JOIN payment ON payment.rental_id = rental.rental_id
-- WHERE rental.return_date IS NULL
-- ORDER BY amount ASC LIMIT 30

-- 6.1
-- SELECT film.title, film.description, actor.first_name, actor.last_name
-- FROM film
-- INNER JOIN film_actor ON film_actor.film_id = film.film_id
-- INNER JOIN actor ON actor.actor_id = film_actor.actor_id
-- WHERE film.description LIKE '%Sumo Wrestler%' and actor.first_name = 'Penelope' and actor.last_name = 'Monroe'

-- 6.2
-- SELECT title, description, length, rating
-- FROM film
-- WHERE rating = 'R' and length = 60

-- 6.3
-- SELECT DISTINCT film.title, film.description
-- FROM film
-- INNER JOIN inventory ON inventory.film_id = film.film_id
-- INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN customer ON rental.customer_id = customer.customer_id
-- INNER JOIN payment ON payment.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew' 
-- and customer.last_name = 'Mahan' 
-- and payment.amount > 4 
-- and rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';


-- 6.4
-- SELECT DISTINCT film.title, film.description, film.replacement_cost
-- FROM film
-- INNER JOIN inventory ON inventory.film_id = film.film_id
-- INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew' 
-- and customer.last_name = 'Mahan' 
-- and film.title LIKE '%Boat%' or film.description LIKE '%Boat%'
-- and film.replacement_cost > 29







