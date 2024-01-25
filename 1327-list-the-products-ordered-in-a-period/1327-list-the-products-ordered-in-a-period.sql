# Write your MySQL query statement below
SELECT product_name, SUM(Orders.unit) AS unit
FROM Products
RIGHT JOIN Orders ON Products.product_id = Orders.product_id
WHERE Orders.order_date LIKE '2020-02%'
GROUP BY product_name
HAVING unit >= 100;