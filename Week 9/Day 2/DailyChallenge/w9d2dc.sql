-- Daily Challenge : Advanced Movie Data Analysis

-- # 1 Calculate the Average Budget Growth Rate for Each Production Company

-- WITH budget_growth AS (
--     SELECT 
--         pc.company_id,
--         pc.company_name,
--         m.movie_id,
--         m.budget,
--         LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date) AS prev_budget,
--         (m.budget - LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date))::NUMERIC / NULLIF(LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date), 0) AS growth_rate
--     FROM 
--         movies.movie_company mc
--     INNER JOIN 
--         movies.production_company pc ON mc.company_id = pc.company_id
--     INNER JOIN 
--         movies.movie m ON mc.movie_id = m.movie_id
-- )
-- SELECT 
--     company_name,
--     AVG(growth_rate) AS avg_budget_growth_rate
-- FROM 
--     budget_growth
-- WHERE 
--     growth_rate IS NOT NULL
-- GROUP BY 
--     company_name
-- ORDER BY 
--     avg_budget_growth_rate DESC


-- # 2 Determine the Most Consistently High-Rated Actor

-- WITH avg_movie_rating AS (
--     SELECT 
--         AVG(m.vote_average) AS overall_avg_rating
--     FROM 
--         movies.movie m
-- ),
-- high_rated_movies AS (
--     SELECT 
--         mc.person_id,
--         p.person_name,
--         COUNT(DISTINCT m.movie_id) AS high_rated_movie_count
--     FROM 
--         movies.movie_cast mc
--     INNER JOIN 
--         movies.movie m ON mc.movie_id = m.movie_id
--     INNER JOIN 
--         movies.person p ON mc.person_id = p.person_id
--     CROSS JOIN 
--         avg_movie_rating amr
--     WHERE 
--         m.vote_average > amr.overall_avg_rating
--     GROUP BY 
--         mc.person_id, p.person_name
-- )
-- SELECT 
--     person_name,
--     high_rated_movie_count
-- FROM 
--     high_rated_movies
-- ORDER BY 
--     high_rated_movie_count DESC
-- LIMIT 1
	
-- # 3 Calculate the Rolling Average Revenue for Each Genre

-- SELECT 
--     g.genre_name,
--     m.title,
--     m.revenue,
--     AVG(m.revenue) OVER (
--         PARTITION BY g.genre_name 
--         ORDER BY m.release_date 
--         ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
--     ) AS rolling_avg_revenue
-- FROM 
--     movies.movie_genres mg
-- INNER JOIN 
--     movies.movie m ON mg.movie_id = m.movie_id
-- INNER JOIN 
--     movies.genre g ON mg.genre_id = g.genre_id
-- ORDER BY 
--     g.genre_name, m.release_date


-- # 4 Identify the Highest-Grossing Movie Series

-- WITH series_revenue AS (
--     SELECT 
--         k.keyword_name AS series_name,
--         SUM(m.revenue) AS total_revenue
--     FROM 
--         movies.movie_keywords mk
--     INNER JOIN 
--         movies.keyword k ON mk.keyword_id = k.keyword_id
--     INNER JOIN 
--         movies.movie m ON mk.movie_id = m.movie_id
--     GROUP BY 
--         k.keyword_name
-- )
-- SELECT 
--     series_name,
--     total_revenue
-- FROM 
--     series_revenue
-- ORDER BY 
--     total_revenue DESC
-- LIMIT 1




