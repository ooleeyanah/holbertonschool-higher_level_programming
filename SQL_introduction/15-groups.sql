-- counts num of records with same score
SELECT score, COUNT(score) AS number FROM second_table ORDER BY score DESC;