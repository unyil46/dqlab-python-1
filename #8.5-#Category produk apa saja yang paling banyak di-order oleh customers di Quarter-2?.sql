#Category produk apa saja yang paling banyak di-order oleh customers di Quarter-2?
#https://academy.dqlab.id/main/livecode/246/421/2108?pr=0
SELECT
  left(productcode, 3) as categoryid,
  count(distinct ordernumber) as total_order,
  sum(quantity) as total_penjualan
FROM
  (
    SELECT
      productcode,
      ordernumber,
      quantity,
      status,
      left(productcode, 3) as categoryid
    FROM
      orders_2
    WHERE
      status = "Shipped"
  ) tabel_c
GROUP BY
  left(productcode, 3)
ORDER BY
  count(distinct ordernumber, categoryid) desc
