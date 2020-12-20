-- SQL - More queries
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN state ON cities.state_id=state.id
GROUP BY id;