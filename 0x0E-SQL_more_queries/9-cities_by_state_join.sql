-- lists all cities
-- displays cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ORDER BY cities.id;
