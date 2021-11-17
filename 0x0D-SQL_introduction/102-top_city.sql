-- 0x0D. SQL introduction, task 19

-- top three cities during July and August ordered by average temperature
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE(month=7 or month=8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
