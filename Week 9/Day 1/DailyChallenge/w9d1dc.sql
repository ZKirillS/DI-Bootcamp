-- SET search_path TO olympics
-- Exercise 1: Detailed Medal Analysis
-- # Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.

-- CREATE TEMP TABLE competitors_medals_seasons (
--     person_id INTEGER,
--     medals_winter INTEGER,
-- 	   medals_summer INTEGER
-- )

-- INSERT INTO competitors_medals_seasons (person_id, medals_summer, medals_winter)
-- SELECT 
--     gc.person_id,
--     SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS medals_summer,
--     SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS medals_winter
-- FROM 
--     competitor_event ce
-- JOIN 
--     games_competitor gc ON ce.competitor_id = gc.person_id
-- JOIN 
--     games g ON gc.games_id = g.id
-- WHERE 
--     ce.medal_id IS NOT NULL
-- GROUP BY 
--     gc.person_id
-- HAVING 
--     SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) > 0
--     AND SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) > 0

-- SELECT * FROM competitor_event
-- SELECT * FROM competitors_medals_seasons

-- # 2 Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.

-- CREATE TEMP TABLE competitors_two_sports (
-- 	person_id INTEGER,
-- 	total_medals INTEGER
-- )

-- INSERT INTO competitors_two_sports (person_id, total_medals)
-- SELECT
-- 	gc.person_id,
-- 	COUNT(DISTINCT ce.event_id) AS total_medals
-- FROM 
-- 	competitor_event ce
-- JOIN games_competitor gc ON ce.competitor_id = gc.person_id
-- JOIN event e ON ce.event_id = e.id
-- WHERE
-- 	ce.medal_id IS NOT NULL
-- GROUP BY
-- 	gc.person_id
-- HAVING
-- 	COUNT(DISTINCT e.sport_id) = 2

-- SELECT
-- 	cts.person_id,
-- 	cts.total_medals
-- FROM competitors_two_sports cts
-- ORDER BY cts.total_medals DESC
-- LIMIT 3
	
-- SELECT * FROM competitors_two_sports

-- Exercise 2: Region and Competitor Performance
-- # 1  Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.

-- WITH competitor_max_total_medals AS (
-- 	SELECT ce.competitor_id,
-- 	   	   ce.event_id,
-- 	   	   COUNT(ce.medal_id) AS total_medals_region
-- FROM competitor_event ce
-- WHERE ce.medal_id IS NOT NULL
-- GROUP BY ce.competitor_id, ce.event_id),

-- max_medals_competitor AS (
-- SELECT competitor_id,
-- 	   event_id,
-- 	   total_medals_region
-- FROM (
-- 	   SELECT
-- 	   		competitor_id,
-- 			event_id,
-- 			total_medals_region,
-- 			RANK() OVER (PARTITION BY competitor_id
-- 			ORDER BY total_medals_region DESC) AS rank
-- 	   FROM competitor_max_total_medals	
-- 	   ) ranked
-- 	   WHERE rank = 1
-- )

-- SELECT 
--     nr.region_name,
--     SUM(medals.total_medals_region) AS total_medals
-- FROM max_medals_competitor medals
-- JOIN games_competitor gc ON medals.competitor_id = gc.person_id
-- JOIN person_region pr ON gc.person_id = pr.person_id
-- JOIN noc_region nr ON pr.region_id = nr.id
-- GROUP BY nr.region_name
-- ORDER BY total_medals DESC
-- LIMIT 5


-- # 2 Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.

-- CREATE TEMP TABLE competitors_three_games (
-- 	full_name VARCHAR(500),
-- 	total_games_0_wins INTEGER DEFAULT 0
-- )

-- INSERT INTO competitors_three_games (full_name, total_games_0_wins)
-- SELECT 
--     p.full_name,
--     COUNT(DISTINCT gc.games_id) AS total_games_0_wins
-- FROM games_competitor gc
-- JOIN person p ON gc.person_id = p.id
-- LEFT JOIN competitor_event ce ON gc.person_id = ce.competitor_id
-- WHERE ce.medal_id = 4
-- GROUP BY p.full_name, gc.person_id
-- HAVING COUNT(DISTINCT gc.games_id) > 3

-- DROP TABLE IF EXISTS competitors_three_games
SELECT * FROM competitors_three_games
ORDER BY total_games_0_wins DESC
LIMIT 10
-- SELECT * FROM competitor_event
-- SELECT * FROM medal