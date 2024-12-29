-- SET search_path TO olympics

-- Exercise 1: Complex Subquery Analysis
-- # 1 Find the Average Age of Competitors Who Have Won at Least One Medal, Grouped by the Type of Medal They Won
-- SELECT * FROM medal
-- SELECT * FROM games_competitor

-- SELECT m.medal_name,
--        AVG(gc.age) AS average_age
-- FROM medal m
-- JOIN games_competitor gc ON m.id = gc.id
-- WHERE EXISTS (
--     SELECT 1
--     FROM medal m2
--     WHERE m2.id = gc.id
--     AND m2.medal_name IS NOT NULL
-- )
-- GROUP BY m.medal_name

-- # 2 Identify the Top 5 Regions with the Highest Number of Unique Competitors Who Have Participated in More Than 3 Different Events
-- SELECT * FROM noc_region

-- SELECT r.region_name,
--        COUNT(DISTINCT p.id) AS unique_competitors
-- FROM noc_region r
-- JOIN person_region pr ON r.id = pr.region_id
-- JOIN person p ON pr.person_id = p.id
-- JOIN (
--     SELECT gc.person_id
--     FROM games_competitor gc
--     GROUP BY gc.person_id
--     HAVING COUNT(DISTINCT gc.games_id) > 3
-- ) AS filtered_competitors ON p.id = filtered_competitors.person_id
-- GROUP BY r.region_name
-- ORDER BY unique_competitors DESC
-- LIMIT 5

-- SELECT * FROM person_region
-- SELECT * FROM person
-- SELECT * FROM competitor_event


-- # 3 Create a Temporary Table to Store the Total Number of Medals Won by Each Competitor and Filter to Show Only Those Who Have Won More Than 2 Medals
-- SELECT * FROM medal

-- CREATE TEMPORARY TABLE competitor_medals AS
-- SELECT ce.competitor_id,
--        COUNT(*) AS total_medals
-- FROM competitor_event ce
-- JOIN medal m ON ce.medal_id = m.id
-- GROUP BY ce.competitor_id
-- HAVING COUNT(*) > 2

-- SELECT * FROM competitor_medals

-- DROP TABLE IF EXISTS competitor_medals

-- # 4 Use a Subquery Within a DELETE Statement to Remove Records of Competitors Who Have Not Won Any Medals from a Temporary Table

-- DELETE FROM competitor_medals
-- WHERE competitor_id NOT IN (
--     SELECT ce.competitor_id
--     FROM competitor_event ce
--     JOIN medal m ON ce.medal_id = m.id
--     WHERE m.id IS NOT NULL
-- )

-- SELECT * FROM competitor_medals


-- EXERCISE 2
-- # 1 Update the Heights of Competitors Based on the Average Height of Competitors from the Same Region Using a Correlated Subquery

-- WITH avg_heights AS (
--     SELECT 
--         pr.region_id, 
--         AVG(p.height) AS avg_height
--     FROM 
--         person p
--     JOIN 
--         person_region pr 
--         ON p.id = pr.person_id
--     WHERE 
--         p.height IS NOT NULL
--     GROUP BY 
--         pr.region_id
-- )
-- UPDATE person
-- SET height = ah.avg_height
-- FROM person_region pr
-- JOIN avg_heights ah ON pr.region_id = ah.region_id
-- WHERE person.id = pr.person_id
--   AND person.height IS NOT NULL


-- SELECT * FROM person_region

-- # 2 Insert New Records Into a Temporary Table for Competitors Who Participated in More Than One Event in the Same Games and List Their Total Number of Events Participated

-- CREATE TEMP TABLE competitor_event_count (
--     person_id INTEGER,
--     games_id INTEGER,
--     total_events INTEGER
-- )

-- INSERT INTO competitor_event_count (person_id, games_id, total_events)
-- SELECT 
--     ce.competitor_id AS person_id,
--     gc.games_id AS games_id,
--     COUNT(DISTINCT ce.event_id) AS total_events
-- FROM 
--     competitor_event ce
-- JOIN 
--     games_competitor gc ON ce.competitor_id = gc.person_id
-- GROUP BY 
--     ce.competitor_id, gc.games_id
-- HAVING 
--     COUNT(DISTINCT ce.event_id) > 1

-- SELECT * FROM competitor_event_count


-- # 3 Identify regions where the average number of medals won per competitor is greater than the overall average number of medals won per competitor. Use subqueries to calculate and compare averages.

-- SELECT 
--     nr.region_name,
--     region_avg.avg_medals_per_competitor
-- FROM (
--     SELECT 
--         pr.region_id,
--         AVG(medals_count.total_medals) AS avg_medals_per_competitor
--     FROM 
--         person_region pr
--     JOIN (
-- 		SELECT 
--             ce.competitor_id AS person_id,
--             COUNT(ce.medal_id) AS total_medals
--         FROM 
--             competitor_event ce
--         WHERE 
--             ce.medal_id IS NOT NULL
--         GROUP BY 
--             ce.competitor_id
--     ) medals_count ON pr.person_id = medals_count.person_id
--     GROUP BY 
--         pr.region_id
-- ) region_avg
-- JOIN noc_region nr ON region_avg.region_id = nr.id
-- WHERE 
-- 	region_avg.avg_medals_per_competitor > (
--         SELECT 
--             AVG(total_medals) 
--         FROM (
-- 			SELECT 
--                 COUNT(ce.medal_id) AS total_medals
--             FROM 
--                 competitor_event ce
--             WHERE 
--                 ce.medal_id IS NOT NULL
--             GROUP BY 
--                 ce.competitor_id
--         ) overall_avg_medals
--     ) ORDER BY avg_medals_per_competitor DESC

-- # 4 Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games.
-- CREATE TEMP TABLE competitors_seasons (
--     person_id INTEGER,
--     seasons TEXT
-- )

-- INSERT INTO competitors_seasons (person_id, seasons)
-- SELECT 
--     gc.person_id,
--     STRING_AGG(DISTINCT g.season, ',') AS seasons
-- FROM 
--     games_competitor gc
-- JOIN 
--     games g ON gc.games_id = g.id
-- GROUP BY 
--     gc.person_id

-- SELECT 
--     cs.person_id
-- FROM 
--     competitors_seasons cs
-- WHERE 
--     cs.seasons LIKE '%Summer%' AND cs.seasons LIKE '%Winter%'

