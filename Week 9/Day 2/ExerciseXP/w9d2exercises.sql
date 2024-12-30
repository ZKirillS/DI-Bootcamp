-- SET search_path TO movies, public;

-- SELECT * FROM genre
-- Exercise 1
-- # 1 Rank Movies by Popularity within Each Genre
-- SELECT
--     g.genre_name,
--     m.title AS movie_title,
--     RANK() OVER (PARTITION BY g.genre_id ORDER BY m.popularity DESC) AS rank_within_genre
-- FROM
--     movie_genres mg
-- JOIN
--     movie m ON mg.movie_id = m.movie_id
-- JOIN
--     genre g ON mg.genre_id = g.genre_id


-- # 2 Identify the Top 3 Movies by Revenue within Each Production Company
-- WITH ranked_movies AS (
--     SELECT 
--         pc.company_name,
--         m.title AS movie_title,
--         m.revenue,
--         NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS revenue_quartile
--     FROM 
--         movies.movie m
--     INNER JOIN 
--         movies.movie_company mc ON m.movie_id = mc.movie_id
--     INNER JOIN 
--         movies.production_company pc ON mc.company_id = pc.company_id
-- )
-- SELECT 
--     company_name,
--     movie_title,
--     revenue,
--     revenue_quartile
-- FROM 
--     ranked_movies
-- WHERE 
--     revenue_quartile <= 3
-- ORDER BY 
--     company_name, revenue DESC


-- # 3 Calculate the Running Total of Movie Budgets for Each Genre
-- SELECT
--     g.genre_name,
--     m.title AS movie_title,
--     m.budget,
--     SUM(m.budget) OVER (PARTITION BY g.genre_id ORDER BY m.title) AS running_total_budget
-- FROM
--     movie_genres mg
-- JOIN
--     movie m ON mg.movie_id = m.movie_id
-- JOIN
--     genre g ON mg.genre_id = g.genre_id

-- # 4 Identify the Most Recent Movie for Each Genre
-- SELECT DISTINCT
--     g.genre_name,
--     FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_id ORDER BY m.release_date DESC) AS most_recent_movie,
--     MAX(m.release_date) OVER (PARTITION BY g.genre_id) AS release_date
-- FROM
--     movie_genres mg
-- JOIN
--     movie m ON mg.movie_id = m.movie_id
-- JOIN
--     genre g ON mg.genre_id = g.genre_id


-- Exercise 2
-- # 1 Rank Actors by Their Appearance in Movies
-- SELECT 
--     p.person_name AS actor_name,
--     COUNT(mc.movie_id) AS movie_count,
--     DENSE_RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC) AS rank
-- FROM 
--     movies.movie_cast mc
-- INNER JOIN 
--     movies.person p ON mc.person_id = p.person_id
-- GROUP BY 
--     p.person_name
-- ORDER BY 
--     rank

-- # 2 Identify the Top Director by Average Movie Rating
-- WITH director_ratings AS (
--     SELECT 
--         p.person_name AS director_name,
--         AVG(m.vote_average) AS avg_rating
--     FROM 
--         movies.movie_crew mc
--     INNER JOIN 
--         movies.person p ON mc.person_id = p.person_id
--     INNER JOIN 
--         movies.movie m ON mc.movie_id = m.movie_id
--     WHERE 
--         mc.department_id = (SELECT department_id FROM movies.department WHERE department_name = 'Directing')
--     GROUP BY 
--         p.person_name
-- )
-- SELECT 
--     director_name,
--     avg_rating
-- FROM 
--     director_ratings
-- ORDER BY 
--     avg_rating DESC
-- LIMIT 1


-- # 3 Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- SELECT 
--     p.person_name AS actor_name,
--     SUM(m.revenue) AS cumulative_revenue
-- FROM 
--     movies.movie_cast mc
-- INNER JOIN 
--     movies.person p ON mc.person_id = p.person_id
-- INNER JOIN 
--     movies.movie m ON mc.movie_id = m.movie_id
-- GROUP BY 
--     p.person_name
-- ORDER BY 
--     cumulative_revenue DESC

-- # 4 Identify the Director Whose Movies Have the Highest Total Budget

-- WITH director_budgets AS (
--     SELECT 
--         p.person_name AS director_name,
--         SUM(m.budget) AS total_budget
--     FROM 
--         movies.movie_crew mc
--     INNER JOIN 
--         movies.person p ON mc.person_id = p.person_id
--     INNER JOIN 
--         movies.movie m ON mc.movie_id = m.movie_id
--     WHERE 
--         mc.department_id = (SELECT department_id FROM movies.department WHERE department_name = 'Directing')
--     GROUP BY 
--         p.person_name
-- )
-- SELECT 
--     director_name,
--     total_budget
-- FROM 
--     director_budgets
-- ORDER BY 
--     total_budget DESC
-- LIMIT 1


