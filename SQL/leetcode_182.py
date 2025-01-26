#PostgreSQL query
SELECT email as Email
FROM Person
GROUP BY email HAVING Count(*) > 1