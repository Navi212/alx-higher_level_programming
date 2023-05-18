-- A script that lists the number of records with the same score in the second_table
-- Code implementation.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
