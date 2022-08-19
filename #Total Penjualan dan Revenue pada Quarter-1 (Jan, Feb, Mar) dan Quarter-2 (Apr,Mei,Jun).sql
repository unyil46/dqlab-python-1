
#Total Penjualan dan Revenue pada Quarter-1 (Jan, Feb, Mar) dan Quarter-2 (Apr,Mei,Jun)
#https://academy.dqlab.id/main/livecode/246/420/2103?pr=0
#SELECT * FROM orders_1 limit 5;
#SELECT * FROM orders_2 limit 5;
#SELECT * FROM customer limit 5;
SELECT sum(quantity) AS total_penjualan
	,sum(quantity * priceeach) as revenue
FROM orders_1
WHERE status="Shipped";

SELECT sum(quantity) AS total_penjualan
	,sum(quantity * priceeach) as revenue
FROM orders_2
WHERE status="Shipped";
