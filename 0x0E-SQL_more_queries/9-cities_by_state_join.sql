-- SQL - More queries
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN state ON cities.state_id=states.id
GROUP BY id;