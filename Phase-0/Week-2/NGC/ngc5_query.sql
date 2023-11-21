SELECT customer_name, count(customer_name) as total_order
FROM Orders JOIN Customers ON Orders.customer_id = Customers.customer_id
GROUP BY customer_name