 -- Query 1: Count and Percentage of Orders Purchased in Jan 2018 with 5 Review Score
 -- olist_orders purchase_timestamp 01-2018, order ID count,
 -- order_reviews review_score 5, % score 5 of all 01-2018 orders
SELECT COUNT(oo.order_id) AS order_count,
 		(COUNT(oo.order_id) * 100.0 / (
         SELECT COUNT(*)
         FROM olist_orders
         WHERE strftime('%Y', order_purchase_timestamp) ='2018'
         AND strftime('%m', order_purchase_timestamp) = '01')
        ) AS percentage 
FROM olist_orders oo
JOIN olist_order_reviews oor ON oo.order_id = oor.order_id
WHERE strftime('%Y', oo.order_purchase_timestamp) ='2018'
AND strftime('%m', oo.order_purchase_timestamp) = '01'
AND oor.review_score = 5


-- Query 2: Customer Purchase Trend Year-on-Year
-- olist_orders time, customer_id, order_status
SELECT strftime('%Y', order_purchase_timestamp) AS year,
       COUNT(DISTINCT customer_id) AS unique_customers,
       COUNT(order_id) AS total_orders
FROM olist_orders
WHERE order_status = 'delivered'
GROUP BY strftime('%Y', order_purchase_timestamp)
ORDER BY year

-- Query 3: Average Order Values of Customers
-- olistolist_orders customer_id, order_items customer_id, price
SELECT customer_id,
	   AVG(order_total) AS avg_order_value
FROM (SELECT oo.order_id,
      		 oo.customer_id,
      		 SUM(ooi.price) AS order_total
      FROM olist_orders oo
      JOIN olist_order_items ooi ON oo.order_id = ooi.order_id
      GROUP BY oo.order_id) AS total_per_order
GROUP BY customer_id
      
-- Query 4: Top 5 Cities with Highest Revenue from 2016 to 2018
-- olist_order_payments - payment_value, order_id,   olist_order_items - order_id, seller_id,
-- olist_orders - order_purchase_timestamp, order_id, olist_sellers - seller_id, seller_city

SELECT os.seller_city,
       SUM(oop.payment_value) AS total_revenue
FROM olist_order_payments oop
JOIN olist_orders oo ON oop.order_id = oo.order_id
JOIN olist_order_items ooi ON oo.order_id = ooi.order_id
JOIN olist_sellers os ON ooi.seller_id = os.seller_id
WHERE strftime('%Y', oo.order_purchase_timestamp) BETWEEN '2016' AND '2018'
GROUP BY os.seller_city
ORDER BY total_revenue DESC
LIMIT 5

-- Query 5: State Wise Revenue Table Between 2016 to 2018
-- olist_order_payments - payment_value, order_id, olist_orders - order_purchase_timestamp, 
-- order_id, customer_id,  olist_customers - customer_id, customer_state

SELECT oc.customer_state,
       SUM(oop.payment_value) AS total_revenue_state
FROM olist_order_payments oop
JOIN olist_orders oo ON oop.order_id = oo.order_id
JOIN olist_customers oc ON oo.customer_id = oc.customer_id
WHERE strftime('%Y', oo.order_purchase_timestamp) BETWEEN '2016' AND '2018'
GROUP BY oc.customer_state
ORDER BY total_revenue_state DESC


-- Query 6: Top Successful Sellers in Terms of Goods Sold, Revenue, and Customer Count
-- olist_orders - customer_id, order_id, olist_olist_order_items - order_id, seller_id,
-- price, olist_olist_order_reviews - order_id, review_score

SELECT ooi.seller_id,
       COUNT(ooi.order_item_id) AS goods_sold,
       SUM(ooi.price) AS total_revenue,
       COUNT(DISTINCT oo.customer_id) AS customer_count,
       SUM(CASE WHEN oor.review_score = 5 THEN 1 ELSE 0 END) AS five_star_reviews
FROM olist_order_items ooi
JOIN olist_orders oo ON ooi.order_id = oo.order_id
JOIN olist_order_reviews oor ON ooi.order_id = oor.order_id
GROUP BY ooi.seller_id
ORDER BY total_revenue DESC
LIMIT 5

SELECT ooi.seller_id,
       COUNT(ooi.order_item_id) AS goods_sold,
       SUM(ooi.price) AS total_revenue,
       COUNT(DISTINCT oo.customer_id) AS customer_count,
       SUM(CASE WHEN oor.review_score = 5 THEN 1 ELSE 0 END) AS five_star_reviews
FROM olist_order_items ooi
JOIN olist_orders oo ON ooi.order_id = oo.order_id
JOIN olist_order_reviews oor ON ooi.order_id = oor.order_id
GROUP BY ooi.seller_id
ORDER BY goods_sold DESC
LIMIT 5

SELECT ooi.seller_id,
       COUNT(ooi.order_item_id) AS goods_sold,
       SUM(ooi.price) AS total_revenue,
       COUNT(DISTINCT oo.customer_id) AS customer_count,
       SUM(CASE WHEN oor.review_score = 5 THEN 1 ELSE 0 END) AS five_star_reviews
FROM olist_order_items ooi
JOIN olist_orders oo ON ooi.order_id = oo.order_id
JOIN olist_order_reviews oor ON ooi.order_id = oor.order_id
GROUP BY ooi.seller_id
ORDER BY customer_count DESC
LIMIT 5


SELECT ooi.seller_id,
       COUNT(ooi.order_item_id) AS goods_sold,
       SUM(ooi.price) AS total_revenue,
       COUNT(DISTINCT oo.customer_id) AS customer_count,
       SUM(CASE WHEN oor.review_score = 5 THEN 1 ELSE 0 END) AS five_star_reviews
FROM olist_order_items ooi
JOIN olist_orders oo ON ooi.order_id = oo.order_id
JOIN olist_order_reviews oor ON ooi.order_id = oor.order_id
GROUP BY ooi.seller_id
ORDER BY five_star_reviews DESC
LIMIT 5

-- Query 7: Delivery Success Rate Across States
-- olist_customers - customer_id, customer_state, olist_orders - customer_id, order_status

SELECT oc.customer_state,
       (SUM(CASE WHEN oo.order_status = 'delivered' THEN 1 ELSE 0 END)
        * 100.0) / COUNT(oo.order_id) AS delivery_success_rate
FROM olist_orders oo
JOIN olist_customers oc ON oo.customer_id = oc.customer_id
GROUP BY oc.customer_state


-- Query 8: Preferred Form of Payment for Different Categories
-- olist+olist_order_payments - payment_type, order_id, olist_order_items - order_id, product_id,
-- olist_ruducts - product_id, porduct_category_name

SELECT op.product_category_name,
       oop.payment_type,
       COUNT(*) AS payment_count
FROM olist_order_items ooi
JOIN olist_products op ON ooi.product_id = op.product_id
JOIN olist_order_payments oop ON ooi.order_id = oop.order_id
GROUP BY op.product_category_name, oop.payment_type
ORDER BY payment_count DESC


