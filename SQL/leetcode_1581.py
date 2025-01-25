#PostgreSQL query
SELECT  customer_id,
        COUNT(*) - COUNT(Transactions.transaction_id) AS count_no_trans
FROM Visits LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
GROUP BY customer_id HAVING COUNT(*) - COUNT(Transactions.transaction_id) > 0


