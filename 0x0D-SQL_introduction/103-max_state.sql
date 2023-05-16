-- A script that displays the maximum temperature of each state
-- Displays the max temperature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
LIMIT 3;
