# Product analysis
It helps for optimise products list, prepare stocks and specify marketing stragegy or website design
for each product/product lines.

## Question 12

Pull monthly trends to date for number of sales, total revenue, and total margin generated
for the business.

_Received date: Jan 04, 2013_

#### SQL query 
```
SELECT
	YEAR(created_at) AS year,
	MONTH(created_at) AS month,
	COUNT(DISTINCT order_id) AS number_of_sales,
	SUM(price_usd) AS total_revenue,
	SUM(price_usd-cogs_usd) AS total_profit
FROM orders
WHERE 
	created_at < '2013-01-04'
GROUP BY
	YEAR(created_at),
	MONTH(created_at);
```
#### Command & Results

```
python3 connect.py --question 12 --db 'mavenfuzzyfactory user password' -task 'run'
```

![image](https://user-images.githubusercontent.com/114192113/211810117-7a31e2a9-6f37-40e3-9299-d6beb001d52f.png)

![image](https://user-images.githubusercontent.com/114192113/211812335-ac620bde-0b2f-4115-881a-eba3fede6c45.png)

#### Comments

The Mr.Fuzzy product had a steadily inrease in orders which brought rises of revenue and profit as well.
The orders increased supprisingly in Nov and was back to normal speed in Dec.

Note: the company used this data as baseline to test new product launching.

## Question 13

The company introduced a new product - Love bear in Jan 2013.
Pull monthly order volume, overall conversion rates, revenue per session, and a 
breakdown of sales by product, all for the time period since April 1, 2012 to compare the 2 products.

_Received date: Apr 10, 2013_

#### SQL query 
```
SELECT
	YEAR(ws.created_at) AS year,
	MONTH(ws.created_at) AS month,
	COUNT(DISTINCT ws.website_session_id) AS sessions,
	COUNT(DISTINCT o.order_id) AS orders,
	COUNT(DISTINCT o.order_id)/COUNT(DISTINCT ws.website_session_id) AS conv_rate,
	SUM(o.price_usd)/COUNT(DISTINCT ws.website_session_id) AS revenue_per_session,
	COUNT(DISTINCT CASE WHEN o.primary_product_id=1 THEN o.order_id ELSE NULL END) AS product_1_orders,
	COUNT(DISTINCT CASE WHEN o.primary_product_id=2 THEN o.order_id ELSE NULL END) AS product_2_orders
FROM website_sessions ws
LEFT JOIN orders o
	ON ws.website_session_id = o.website_session_id
WHERE 
	ws.created_at < '2013-04-05' 
	AND ws.created_at >'2012-04-01'
GROUP BY 1,2;
```
#### Command & Results

```
python3 connect.py --question 13 --db 'mavenfuzzyfactory user password' -task 'run'
```

![image](https://user-images.githubusercontent.com/114192113/211821591-f4d96e93-7d69-446a-9dbe-d887638e84e4.png)

![image](https://user-images.githubusercontent.com/114192113/211846815-fbf76734-a1fa-4056-ae68-d4f411da8f8d.png)

#### Comments
After holiday, the orders reduced and fluctuated.
Since the new product lanching in Jan 2013, the Mr.Fuzzy orders decreased and stayed stable while 
the Love Bear orders were not stable.

Note: the full data for the last month had not been collected yet.
