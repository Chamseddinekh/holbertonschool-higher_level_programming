-- show databases
-- because Batch 3 is the best!
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;