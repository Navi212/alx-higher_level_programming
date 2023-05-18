-- A script that lists all records with a score >= 10 in the scond_table DB hbtn_0c_0
-- Code implementation.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
