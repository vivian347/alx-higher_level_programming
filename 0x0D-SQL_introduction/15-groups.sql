-- list number of records with same score in the table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;
