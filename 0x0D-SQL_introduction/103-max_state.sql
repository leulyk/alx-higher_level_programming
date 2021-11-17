-- 0x0D. SQL introduction, Task 20

-- max temperature of each state ordered by state
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
