#Promotion Effectiveness and Efficiency by Years
#https://academy.dqlab.id/main/livecode/182/359/1758?pr=0
SELECT YEAR(order_date) AS years
	,SUM(sales) AS sales
	,SUM(discount_value) as promotion_value
	,ROUND((SUM(discount_value)/SUM(sales)) * 100,2) AS burn_rate_percentage
FROM dqlab_sales_store
WHERE order_status="Order Finished"
GROUP BY years
ORDER BY years, SUM(sales) DESC;
#SELECT * FROM dqlab_sales_store LIMIT 2
