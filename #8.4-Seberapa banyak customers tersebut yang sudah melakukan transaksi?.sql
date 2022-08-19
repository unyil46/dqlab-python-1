#Seberapa banyak customers tersebut yang sudah melakukan transaksi?
#https://academy.dqlab.id/main/livecode/246/421/2107?pr=0
#SELECT * FROM customer limit 5;
SELECT
  quarter,
  COUNT(DISTINCT(customerID)) AS total_customers
FROM
  (
    SELECT
      customerID,
      createDate,
      QUARTER(createDate) as quarter
    FROM
      customer
    WHERE
      createDate >= '2004-01-01'
      AND createDate <= '2004-06-30'
  ) AS tabel_b
WHERE
  customerID IN (
    SELECT
      DISTINCT customerID
    FROM
      orders_1
    UNION
    SELECT
      customerID
    FROM
      orders_2
  )
GROUP BY
  quarter;
