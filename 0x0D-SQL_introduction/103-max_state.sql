-- display max temp of each state order by state name
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state;
