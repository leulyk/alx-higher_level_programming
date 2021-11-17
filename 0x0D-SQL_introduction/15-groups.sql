-- 0x0D. SQL introduction, Task 15

-- group by score
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
