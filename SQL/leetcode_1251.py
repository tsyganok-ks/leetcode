#PostgreSQL query
SELECT Prices.product_id,
        COALESCE(ROUND(SUM(UnitsSold.units * Prices.price) *1.00 / SUM(UnitsSold.units),2),0) AS average_price
FROM Prices LEFT JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id
WHERE UnitsSold.purchase_date >= Prices.start_date AND
      UnitsSold.purchase_date <= Prices.end_date
      OR UnitsSold.purchase_date is NULL

GROUP BY Prices.product_id