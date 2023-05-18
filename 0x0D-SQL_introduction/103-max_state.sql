-- A script that displays the max temperature of each state(order by State name)
-- Code implementation.
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
LIMIT 3;
