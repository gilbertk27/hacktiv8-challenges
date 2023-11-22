-- SELECT * from crunchbase_companies_clean_data
-- SELECT * from dc_bikeshare_q1_2012

SELECT 
	LEFT (start_station, 3) as "3rd_l", 
	RIGHT (start_station, 3) as "3rd_r",
	SUBSTR(start_station, 5, 5) as "mid",
	TRIM(both 'y' FROM start_station) as trimer,
	UPPER(start_station) as gede,
	LOWER(start_station) as cilik,
	CONCAT(start_station, ' TO ', end_station)
	start_station	
FROM dc_bikeshare_q1_2012

SELECT CAST(founded_at_clean AS DATE) FROM crunchbase_companies_clean_data

SELECT 
	EXTRACT(DOY FROM CAST(founded_at_clean AS DATE))
FROM crunchbase_companies_clean_data

-- EXTRACT (field from source)
SELECT
	EXTRACT(DAY FROM CAST(founded_at_clean AS DATE)) as date,
	EXTRACT(MONTH FROM CAST(founded_at_clean AS DATE)) AS month,
	EXTRACT(YEAR FROM CAST(founded_at_clean AS DATE)) AS year,
	EXTRACT(DOY FROM CAST(founded_at_clean AS DATE)) AS doy,
	EXTRACT(DOW FROM CAST(founded_at_clean AS DATE)) AS dow
FROM crunchbase_companies_clean_data

SELECT EXTRACT (DOY FROM CAST(NOW() AS DATE))

SELECT name, funding_total_usd 
FROM crunchbase_companies_clean_data
WHERE funding_total_usd IS NOT NULL

-- ingin menambahkan satu column berdasarkan
-- conditional logic yang kamu miliki terhadap data

SELECT
	name,
	funding_total_usd,
	CASE
		WHEN funding_total_usd > 80000000 THEN 'High'
		WHEN funding_total_usd > 50000000 THEN 'Medium'
		ELSE 'LOW'
	END AS category
FROM crunchbase_companies_clean_data
WHERE funding_total_usd IS NOT NULL

SELECT MIN(funding_total_usd) 
FROM crunchbase_companies_clean_data

UPDATE crunchbase_companies_clean_data
SET funding_total_usd = 19299
WHERE city IS NULL

-- !!!!!!!!!!!!!!!!!!!!!!!!!!!! LC!!!!!!!!!!!!!
SELECT *
FROM crunchbase_companies_clean_data
WHERE funding_total_usd = (
	SELECT MIN(funding_total_usd) 
	FROM crunchbase_companies_clean_data
)

SELECT subquery.start_station,
       subquery.trip_count
FROM (
    SELECT start_station,
           COUNT(*) AS trip_count
    FROM dc_bikeshare_q1_2012
    GROUP BY start_station
) AS subquery
ORDER BY subquery.trip_count DESC;

SELECT region, MAX(funding_total_usd)
FROM crunchbase_companies_clean_data
GROUP BY region
HAVING MAX(funding_total_usd) > 1000000

SELECT name,
    status,
    region,
    founded_at,
	funding_total_usd
FROM crunchbase_companies_clean_data AS C
WHERE funding_total_usd IN(
	SELECT MAX(funding_total_usd)
	FROM crunchbase_companies_clean_data
	GROUP BY region
	HAVING MAX(funding_total_usd) > 1000000)
AND founded_at IS NOT NULL;
