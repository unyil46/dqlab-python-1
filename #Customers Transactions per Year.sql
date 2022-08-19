#Customers Transactions per Year
#https://academy.dqlab.id/main/livecode/182/361/1760?pr=0

SELECT YEAR(order_date) AS years
	,COUNT(DISTINCT(customer)) AS number_of_customer
FROM dqlab_sales_store
WHERE order_status="Order Finished"
	AND YEAR(order_date) >= 2009
	AND YEAR(order_date) <= 2012
GROUP BY years
ORDER BY years;
#SELECT * FROM dqlab_sales_store LIMIT 2
