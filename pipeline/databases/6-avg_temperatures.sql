-- display average tempeqature(Fahrenheit) for each city ordered by temp in descending order

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;