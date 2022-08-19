#Menghitung persentasi keseluruhan penjualan
#https://academy.dqlab.id/main/livecode/246/420/2104?pr=0

#SELECT * FROM orders_1 limit 5;
#SELECT * FROM orders_2 limit 5;
#SELECT * FROM customer limit 5;

SELECT
  quarter,
  SUM(quantity) as total_penjualan,
  sum(quantity * priceeach) as revenue
FROM
  (
    SELECT
      orderNumber,
      status,
      quantity,
      priceeach,
      1 as quarter
    FROM
      orders_1
    UNION
    SELECT
      orderNumber,
      status,
      quantity,
      priceeach,
      2 as quarter
    FROM
      orders_2
  ) AS tabel_a
WHERE
  status = "Shipped"
GROUP BY
  quarter;
