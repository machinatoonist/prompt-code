--- Prompt: 
--- Write a SQL query to calculate a 30-day moving average of the 
--- total sales revenue from a table called `sales`.

SELECT item, 
       AVG(total_sales) AS '30-day moving average of total sales'
FROM sales
GROUP BY item
HAVING DATEDIFF(NOW(), date) <= 30