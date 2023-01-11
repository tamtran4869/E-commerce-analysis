# Website performance analysis
At the same time, the marketing team optimises marketing strategy to increase sessions and conversion rate, 
the website team conducts tests on different page designs to reduce bounce rates and increase conversion rates as well.

## Question 7

Pull the most-viewed website pages, ranked by session volume.

_Received date: Jun 09, 2012_

#### SQL query 
```
SELECT 
	pageview_url, 
	COUNT(DISTINCT website_session_id) AS sessions 
FROM website_pageviews 
WHERE 
	created_at < ‘2012-06-09’ 
GROUP BY 
	pageview_url 
ORDER BY
	sessions DESC;
```
#### Command & Results
```
python3 connect.py --question 7 --db 'mavenfuzzyfactory user password' -task 'run'
```

![image](https://user-images.githubusercontent.com/114192113/211772184-5e521eb1-e661-4442-93f1-d2e127be91a4.png)

![image](https://user-images.githubusercontent.com/114192113/211772243-21b12f6b-68e8-49fa-b9b1-d2ca55379bbe.png)

#### Comments
The /home page had the highest number of sessions. The order seemed to follow the user's buying journey. The sessions drop after each step.
It is important to know which step drops the most for optimisation.

## Question 8

Start with landing page /lander-1 (after AB testing, the /lander-1 showed lower bounce rates) and build the funnel to the thank you page using data since August 5.

_Received date: Jun 09, 2012_

#### SQL query 
There are some steps to extract the required data. 

1. Mark the pageview_url with 1 and 0 using window functions >>> page_flag

 ![image](https://user-images.githubusercontent.com/114192113/211776597-2e857799-ad0e-4ca1-b03b-e7036e79665e.png)

2. Group by session id and group by website_session_id and other columns keep the max value. The results show which step of the funnel the website session went through. 
(e.g. session id 24305 made to the second step of the funnel) >>> funnel_flag (using this as a subquery).
![image](https://user-images.githubusercontent.com/114192113/211776782-6cd65c91-d2df-4c94-a78a-78202e77540c.png)

3. The entire session and percentages of each step are compiled. 

![image](https://user-images.githubusercontent.com/114192113/211776889-af0b6c28-8c82-4fb9-ab2b-b8f4b9966612.png)

The full query:
```
-- Create page_flag table
WITH page_flag AS (
SELECT
	ws.website_session_id,
	wp.pageview_url,
	CASE WHEN wp.pageview_url = '/products' THEN 1 ELSE 0 END AS products_page,
	CASE WHEN wp.pageview_url = '/the-original-mr-fuzzy' THEN 1 ELSE 0 END AS mrfuzzy_page,
	CASE WHEN wp.pageview_url = '/cart' THEN 1 ELSE 0 END AS cart_page,
	CASE WHEN wp.pageview_url = '/shipping' THEN 1 ELSE 0 END AS shipping_page,
	CASE WHEN wp.pageview_url = '/billing' THEN 1 ELSE 0 END AS billing_page,
	CASE WHEN wp.pageview_url = '/thank-you-for-your-order' THEN 1 ELSE 0 END AS thankyou_page
FROM website_sessions ws
LEFT JOIN website_pageviews wp
	ON ws.website_session_id = wp.website_session_id
WHERE 
	ws.utm_source = 'gsearch' AND
	ws.utm_campaign = 'nonbrand' AND
	ws.created_at > '2012-08-05' AND
	ws.created_at < '2012-09-05' 
ORDER BY
	ws.website_session_id,
	ws.created_at)

-- Compile metrics from the funnel_flag
SELECT 
	COUNT(website_session_id) AS total_session,
	SUM(to_product) AS to_product,
	SUM(to_product)/COUNT(website_session_id) AS landing_ctr,
	SUM(to_mrfuzzy) AS to_mrfuzzy,
	SUM(to_mrfuzzy)/SUM(to_product) AS product_ctr,
	SUM(to_cart) AS to_cart,
	SUM(to_cart)/SUM(to_mrfuzzy) AS mrfuzzy_ctr,
	SUM(to_shipping) AS to_shipping,
	SUM(to_shipping)/SUM(to_cart) AS cart_ctr,
	SUM(to_billing) AS to_billing,
	SUM(to_billing)/SUM(to_shipping) AS shipping_ctr,
	SUM(to_thankyou) AS to_thankyou,
	SUM(to_thankyou)/SUM(to_billing) AS billing_ctr

FROM (
	SELECT   -- Funnel_flag
		website_session_id,
		MAX(products_page) AS to_product,
		MAX(mrfuzzy_page) AS to_mrfuzzy,
		MAX(cart_page) AS to_cart,
		MAX(shipping_page) AS to_shipping,
		MAX(billing_page) AS to_billing,
		MAX(thankyou_page) AS to_thankyou
	FROM page_flag
	GROUP BY website_session_id
	) AS funnel_flag;
```

Note: In this case, we can not use COUNT and PARTITION BY because it returns distinct sessions of each step but can not show the tunnel path of a specific session.

#### Command & Results
```
python3 connect.py --question 8 --db 'mavenfuzzyfactory user password' -task 'run'
```

![Q8](https://user-images.githubusercontent.com/114192113/211786319-8702de42-41f2-4822-9bf0-a65afeaf0e41.png)

#### Comments

The /lander-1, /mrfuzzy and /billing had low click-throught rates (CTR). It could be the unfriendly designs, unattractive contents (e.g. product images are blurred, information is not catchy, price is high), the complicated payment systems. The team should dig more into these hypothesises. 

## Question 9

Get results from AB testing with /billing and /billing-2

_Received date: Nov 10, 2012_

#### SQL query 
```
SELECT
	pageview_url,
	COUNT(DISTINCT website_session_id) AS sessions,
	COUNT(DISTINCT order_id) AS orders,
	COUNT(DISTINCT order_id)/COUNT(DISTINCT website_session_id) AS conv_rate
FROM 
(
SELECT 
	wp.website_session_id,
	wp.pageview_url, 
	o.order_id
FROM website_pageviews wp
LEFT JOIN orders o
	ON o.website_session_id = wp.website_session_id
WHERE 
	wp.website_pageview_id >= 53550 -- the first pageview id of /billing-2 (starting the test)
	AND wp.created_at < '2012-11-10'
	AND wp.pageview_url IN ('/billing','/billing-2')
) AS billing_data
GROUP BY pageview_url;
```
#### Command & Results
```
python3 connect.py --question 9 --db 'mavenfuzzyfactory user password' -task 'run'
```
![image](https://user-images.githubusercontent.com/114192113/211789640-9110017f-dc47-4428-bf27-6dc425f66caf.png)

#### Comments
It is clear that the new billing page had better performance.
