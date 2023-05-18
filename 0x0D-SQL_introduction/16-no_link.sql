-- A script that lists all records of the table second_table of DB hbtn_0c_0
-- Code implementation.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
