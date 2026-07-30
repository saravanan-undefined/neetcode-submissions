-- Write your query below
SELECT 
    p.first_name as first_name,
    p.last_name as last_name,
    a.city as city,
    a.state as state
FROM person as p
LEFT JOIN address as a
ON p.person_id = a.person_id;