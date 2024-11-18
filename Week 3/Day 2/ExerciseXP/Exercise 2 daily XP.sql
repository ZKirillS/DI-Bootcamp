-- SELECT * FROM customer

-- SELECT CONCAT(first_name,' ',last_name) AS full_name from customer;

-- SELECT DISTINCT create_date FROM customer

-- SELECT * FROM customer ORDER BY first_name DESC

-- SELECT film_id, title, description, release_year, rental_rate 
-- FROM film 
-- ORDER BY rental_rate ASC

-- SELECT address, address2, phone
-- FROM address
-- WHERE district = 'Texas'

-- SELECT * FROM film WHERE film_id = 15 or film_id = 150

-- SELECT film_id, title, description, length, rental_rate
-- FROM film Where title = 'Star Wars'

-- SELECT film_id, title, description, length, rental_rate
-- FROM film WHERE title LIKE 'St%'

-- SELECT * 
-- FROM payment
-- ORDER BY amount ASC LIMIT 10

-- WITH Cheapest AS(
-- SELECT *, ROW_NUMBER() OVER (ORDER BY amount ASC) as row_num
-- FROM payment
-- )
-- SELECT *
-- FROM Cheapest
-- WHERE row_num > 10 and row_num <= 20

-- SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- FROM customer
-- INNER JOIN payment ON customer.customer_id = payment.customer_id
-- ORDER BY customer_id ASC

-- SELECT film.film_id, film.title
-- FROM film
-- LEFT JOIN inventory ON inventory.film_id = film.film_id
-- WHERE inventory.inventory_id IS NULL

-- SELECT city.city, country.country
-- FROM city
-- FULL OUTER JOIN country ON city.country_id = country.country_id
-- ORDER BY country ASC

-- SELECT staff.last_name, payment.staff_id, customer.first_name, customer.last_name,
-- payment.amount, payment.payment_date, customer.customer_id
-- FROM payment
-- INNER JOIN staff ON staff.staff_id = payment.staff_id
-- INNER JOIN customer ON payment.customer_id = customer.customer_id
-- ORDER BY staff_id

















