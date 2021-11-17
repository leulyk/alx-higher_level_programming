-- 0x0D. SQL introduction, Task 16

-- list table but don't list rows with no name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
