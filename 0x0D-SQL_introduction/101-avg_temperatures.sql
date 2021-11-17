-- 0x0D. SQL introduction, Task 18

-- dump a temperatures table and display
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
