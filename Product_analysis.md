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
python3 connect.py --question 12 --db 'mavenfuzzyfactory user password'
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

_Received date: Apr 05, 2013_

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
python3 connect.py --question 13 --db 'mavenfuzzyfactory user password'
```

![image](https://user-images.githubusercontent.com/114192113/211821591-f4d96e93-7d69-446a-9dbe-d887638e84e4.png)

![image](https://user-images.githubusercontent.com/114192113/211849875-00c2c27d-ff02-426d-96b1-113a5a5c5ffe.png)

#### Comments
After holiday, the orders reduced and fluctuated.
Since the new product lanching in Jan 2013, the Mr.Fuzzy orders decreased and stayed stable while 
the Love Bear orders were not stable. 

However, the conversion rates kept going up. It could be the general improvements of business (e.g. due to improve in marketing, website) or the good performance of new product. 

Note: the full data for the last month had not been collected yet.

## Question 14

Pull CTR from /products since the new product launch on 2013-01-06, by product,
and compare to the 3 months leading up to launch as a baseline.

_Received date: Apr 06, 2013_

#### SQL query 
There are some steps to extract the data:
1. Get sessions viewing the /product page and classify it into before and after product 2 launching. 

![image](https://user-images.githubusercontent.com/114192113/211909711-6ab085f8-d943-474e-bb46-779b6c4d1c57.png)

2. Get the next pageview id of these sessions

![image](https://user-images.githubusercontent.com/114192113/211909854-fa02dc51-9f18-4093-b733-8444428dac1e.png)

3. Get url of the next pageviews by the next pageview id.

![image](https://user-images.githubusercontent.com/114192113/211909995-b9ff76f6-8eb6-4893-8b99-217d5172d9f7.png)

4. Compute the count sessions group by the time period

![image](https://user-images.githubusercontent.com/114192113/211912426-f9ab7aa9-fff9-4d46-9e4e-d3165ab2e413.png)

5. Calculate CTR of /products to next pageview, CTR of /products to /the-original-mr-fuzzy and CTR of /products to the /the-forever-love-bear

![image](https://user-images.githubusercontent.com/114192113/211910705-bd7105ea-183c-42d6-b091-7266d02d4d3f.png)

These 5 select statements could be presented in form of cte, subquery or teamporary table depending on different purposes. This project prefers cte and subquery to combine all into 1 query which is more simple for running through Python.

The full SQL query:


```
-- Create cte to get next pageview id from sessions viewing /products.
WITH next_pageview_id AS (
SELECT 
	pp.website_session_id,
	pp.time_period,
	MIN(wp.website_pageview_id) AS next_pageview
FROM 	(
	SELECT -- Get sessions viewing products
		website_session_id,
		website_pageview_id,
		created_at,
		CASE
			WHEN created_at < '2013-01-06' THEN 'A. Before_Product2'
			WHEN created_at >= '2013-01-06' THEN 'B. After_Product2'
			ELSE NULL
		END AS time_period
	FROM website_pageviews
	WHERE 
		created_at < '2013-04-06' AND
		created_at > '2012-10-06' AND
		pageview_url = '/products'
	) AS pp
LEFT JOIN website_pageviews wp
	ON wp.website_session_id  = pp.website_session_id
	AND wp.website_pageview_id > pp.website_pageview_id
GROUP BY 1,2)


-- Compute session counts and CTR 
SELECT 
	time_period,
	sessions,
	next_pageview_sessions,
	next_pageview_sessions/sessions AS next_page_ctr,
	to_mrfuzzy,
	to_mrfuzzy/sessions AS mrfuzzy_ctr,
	to_lovebear,
	to_lovebear/sessions AS lovebear_ctr
FROM 	(
	SELECT -- Count sessions
		time_period,
		COUNT(DISTINCT website_session_id) AS sessions,
		COUNT(DISTINCT CASE WHEN next_pageview_url IS NOT NULL THEN website_session_id ELSE NULL END) AS next_pageview_sessions,
		COUNT(DISTINCT CASE WHEN next_pageview_url = '/the-original-mr-fuzzy' THEN website_session_id ELSE NULL END) AS to_mrfuzzy,
		COUNT(DISTINCT CASE WHEN next_pageview_url = '/the-forever-love-bear' THEN website_session_id ELSE NULL END) AS to_lovebear
	FROM	(	
		SELECT -- Get next pageview url
			npi.website_session_id,
			npi.time_period,
			wp.pageview_url AS next_pageview_url
		FROM next_pageview_id AS npi
		LEFT JOIN website_pageviews wp 
			ON wp.website_pageview_id = npi.next_pageview
		) AS next_pageview_url
	GROUP BY 1
	) AS count_sessions;

```
#### Command & Results

```
python3 connect.py --question 13 --db 'mavenfuzzyfactory user password'
```


#### Comments
It is clear the the percentage of sessions clicking to the next page after seeing the product listing page after launching the love bear product was higher than before. It could be explained by the various choice of products. So, adding more products helps imrpove CTR.

While the percentage of click to the Mr Fuzzy product decreased after adding the love bear, it still accounted for major amounts. Assuming using same marketing stragegy, one possible reason is that the Mr Fuzzy could be siutable for a mass target audience than the Love Bear (e.g. only for couples). 
