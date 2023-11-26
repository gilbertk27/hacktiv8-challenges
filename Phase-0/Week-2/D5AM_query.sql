-- SELECT duration_seconds,
--        SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
--   FROM dc_bikeshare_q1_2012
  
-- SELECT start_terminal,
--    duration_seconds,
--    SUM(duration_seconds) OVER
-- 	 (PARTITION BY start_terminal) AS running_total,
--    COUNT(duration_seconds) OVER
-- 	 (PARTITION BY start_terminal) AS running_count,
--    AVG(duration_seconds) OVER
-- 	 (PARTITION BY start_terminal) AS running_avg
-- FROM dc_bikeshare_q1_2012
-- WHERE start_time < '2012-01-08'

-- SELECT *
-- from (SELECT start_terminal,
--        start_time,
--        duration_seconds,
--        ROW_NUMBER() OVER (ORDER BY start_time desc)
--                     AS rn
--   FROM dc_bikeshare_q1_2012
--  WHERE start_time < '2012-01-08') as sub
--  WHERE rn = 1

-- SELECT start_terminal,
--        duration_seconds,
--        RANK() OVER (PARTITION BY start_terminal
--                     ORDER BY start_time)
--               AS ranking
--   FROM dc_bikeshare_q1_2012
--  WHERE start_time < '2012-01-08'
 
 
--  SELECT start_terminal,
--        duration_seconds,
--        NTILE(4) OVER
--          (PARTITION BY start_terminal ORDER BY duration_seconds)
--          AS quartile
--   FROM dc_bikeshare_q1_2012
--  WHERE start_time < '2012-01-08'
--  ORDER BY start_terminal, duration_seconds


-- BEGIN;

-- CREATE TABLE players (
--     full_school_name VARCHAR(255),
--     school_name VARCHAR(255),
--     player_name VARCHAR(255),
--     position VARCHAR(255),
--     height FLOAT,
--     weight FLOAT,
--     year VARCHAR(255),
--     hometown VARCHAR(255),
--     state VARCHAR(255),
--     id INT PRIMARY KEY
-- );

-- CREATE TABLE teams (
--     division VARCHAR(100),
--     conference VARCHAR(100),
--     school_name VARCHAR(100),
--     roster_url VARCHAR(200),
--     id INT PRIMARY KEY
-- );

-- COMMIT;

-- select * from players

SELECT teams.conference AS conference,
       players.year,
       COUNT(1) AS players
  FROM players
  JOIN teams teams
    ON teams.school_name = players.school_name
 GROUP BY 1,2
 ORDER BY 1,2

SELECT *
  FROM (
        SELECT teams.conference AS conference,
               players.year,
               COUNT(1) AS players
            FROM players players
            JOIN teams
            ON teams.school_name = players.school_name
         GROUP BY 1,2
       ) sub