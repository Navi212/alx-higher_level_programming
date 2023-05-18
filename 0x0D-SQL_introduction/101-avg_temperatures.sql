-- A script that displays the average temperature(Fahrenheit) by city ordered by temp
-- in Descending order in reference to the downloaded file for this Task.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
