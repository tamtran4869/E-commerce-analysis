# Traffic source analysis
## Question 0

Get data to understand where the bulk of the website sessions are coming from, through yesterday and  breakdown by UTM source, campaign and referring domain.

_Received date: Apr 12, 2012_

#### SQL query 
```
SELECT
	utm_source, 
	utm_campaign, 
	http_referer, 
	COUNT(website_session_id) AS sessions
FROM 
	website_sessions 
WHERE 
	created_at < '2012-04-12' 
GROUP BY 
	utm_source, 
	utm_campaign,
	http_referer 
ORDER BY 
  sessions DESC;
```
#### Command & Results
```
python3 connect.py --question 0 --db 'mavenfuzzyfactory user password' -task 'run'
```

![image](https://user-images.githubusercontent.com/114192113/211681955-d43c760b-78cf-448a-b3f7-96a080a81aaf.png)

The data in this question is simple and can devire conclusion without chart.

#### Comments
The traffic from Google search with non-brand keywords are the main source compared to other sources. We should investigate more this to find whether it could get better.

## Question 1

Calculate the conversion rate from session to order? The company needs a conversion rate of at least 4%.

_Received date: Apr 14, 2012_

#### SQL query 
Using window functions
```
WITH cte AS 
(	
	SELECT 
		COUNT(DISTINCT ws.website_session_id) AS sessions, 
		COUNT(DISTINCT o.order_id) AS orders 
	FROM website_sessions ws 
	LEFT JOIN orders o 
		ON o.website_session_id = ws.website_session_id 
	WHERE 
		ws.created_at < '2012-04-14' AND 
		utm_source = 'gsearch’ AND 
		utm_campaign = 'nonbrand'
) 
SELECT *, orders/sessions as conv_rate FROM cte;
```
#### Command & Results
```
python3 connect.py --question 1 --db 'mavenfuzzyfactory user password' -task 'run'
```
![image](https://user-images.githubusercontent.com/114192113/211685203-27a665cd-04ad-4443-85b7-e6578d6ff9dc.png)

The data in this question is simple and can devire conclusion without chart.

#### Comments
It is clear that the conversion rate of Google search - nonbrand source does not meet the requirement.  

## Question 2

Pull gsearch nonbrand trended session volume, by week, to check whether the bid changes (2012-04-15) have caused volume to drop.

_Received date: May 12, 2012_

#### SQL query 
```
SELECT 
	MIN(DATE(created_at)) AS week_start_date, 
	COUNT(DISTINCT website_session_id) AS sessions 
FROM website_sessions 
WHERE 
	created_at < '2012-05-10' AND 
	utm_source = 'gsearch' AND 
	utm_campaign = 'nonbrand' 
GROUP BY 
	YEARWEEK(created_at);
```
#### Command & Results
```
python3 connect.py --question 2 --db 'mavenfuzzyfactory user password' -task 'run'
```

![image](https://user-images.githubusercontent.com/114192113/211686782-4ef44611-f374-44df-9481-494965e3f755.png )

It is more easy to see the trend with a line graph.
![image](https://user-images.githubusercontent.com/114192113/211686883-74edef5c-8d92-4460-aabe-92802b8a314f.png)


#### Comments
The number of sessions go down significantly; hence, the source could be sensitive with bidding price.

## Question 3

Continue with the gsearch-nonbrand, pull conversion rates from session to order, by device type.

_Received date: May 11, 2012_

#### SQL query 
Using window functions
```
WITH cte AS 
(
	SELECT 
		ws.device_type, 
		COUNT(DISTINCT ws.website_session_id) AS sessions, 
		COUNT(DISTINCT o.order_id) AS orders 
	FROM website_sessions ws
	LEFT JOIN orders o 
		ON o.website_session_id = ws.website_session_id 
	WHERE 
		ws.created_at < '2012-05-11' AND 
		utm_source = 'gsearch' AND 
		utm_campaign = 'nonbrand' 
	GROUP BY 
		ws.device_type
) 
SELECT *, orders/sessions as conv_rate 
FROM cte;
```
#### Command & Results
```
python3 connect.py --question 3 --db 'mavenfuzzyfactory user password' -task 'run'
```
![image](https://user-images.githubusercontent.com/114192113/211688365-ad1f4756-48fa-4455-a0be-3448ab0c05d2.png)

The data in this question is simple and can devire conclusion without chart.

#### Comments
Sessions from desktop device tend to generate higher CTR, so to imrpove CTR of the source, from insights from Q2 and Q3, the company could increase budget, bidding for delivering ad in desktop to achieve the expected CTR 4%.

## Question 4

Pull weekly trends for both desktop and mobile of gsearch nonbrand keywords to see the impact on volume due to the change of bid up the channel since 2012-05-19

_Received date: Jun 09, 2012

#### SQL query 
```
SELECT 
	MIN(DATE(created_at)) AS week_start_date, 
	COUNT(DISTINCT CASE WHEN device_type = 'desktop' THEN website_session_id 			ELSE NULL END) AS desktop_sessions, 
	COUNT(DISTINCT CASE WHEN device_type = 'mobile' THEN website_session_id ELSE 		NULL END) AS mobile_sessions 
FROM website_sessions 
WHERE 
	created_at < '2012-06-09' AND 
	created_at > '2012-04-15' AND 
	utm_source = 'gsearch' AND 
	utm_campaign = 'nonbrand' 
GROUP BY 
	YEARWEEK(created_at);
```
#### Command & Results
```
python3 connect.py --question 4 --db 'mavenfuzzyfactory user password' -task 'run'
```

![image](https://user-images.githubusercontent.com/114192113/211763464-5938c477-416c-4d64-bc3f-cc6f6c9d40e4.png)

It is more easy to see the trend with a multiple line graph.
![image](https://user-images.githubusercontent.com/114192113/211763593-79eda6f8-6f33-494b-a9a7-6f359cd6832b.png)

#### Comment
The chart shows a soar of desktop sessions as bidding up while the mobile sessions slightly decrease 
(It could be bidding down for mobile device or there is an inverse relationship with desktop sessions).

## Question 5
For futher investigate into the SEM channels, the company want to optimise the platforms as well.
Compare 2 SEM platform Google & Bing by conversion rate slicing by device type.

_Received date: Dec 01, 2012_

#### SQL query 
```
SELECT 
	ws.device_type,
	ws.utm_source,
	COUNT(DISTINCT ws.website_session_id)  AS sessions,
	COUNT(DISTINCT o.order_id) AS orders,
	COUNT(DISTINCT o.order_id)/COUNT(DISTINCT ws.website_session_id) AS conv_rate
FROM website_sessions ws
LEFT JOIN orders o
	ON o.website_session_id = ws.website_session_id
WHERE 
	ws.created_at > '2012-08-22'
	AND ws.created_at < '2012_09_19'
	AND ws.utm_campaign = 'nonbrand'
GROUP BY 
	ws.device_type,
	ws.utm_source;
```
#### Command & Results
```
python3 connect.py --question 5 --db 'mavenfuzzyfactory user password' -task 'run'
```

![image](https://user-images.githubusercontent.com/114192113/211767130-7811c5f9-4252-4829-b60d-9a06726b139d.png)

#### Comments
Only gsearch-nonbrand-desktop campaign gains the expected CTR. ALthough the bsearch-nonbrand-desktop does not get the CTR 4%, it has significant high CTR. 
As features of SEM, the inventory may be not always available. If the inventory in Google is enough, the team could bid down the bsearch campaign. Otherwise, the team could optimize ad contents to improve CTR on bsearch-nonbrand-desktop.

Ads in Google search in both devices have higher CTR compared to Bing search.

## Question 6
Pull organic search, direct type in, and paid brand search sessions by month, and show those sessionss a % of paid search nonbrand?

_Received date: Dec 23, 2012_

#### SQL query 
Using CASE WHEN to classify into different channels, then subquery to count sessions and group by time and channels.
```
SELECT 
	YEAR(created_at) AS year,
	MONTH(created_at) AS month,
	COUNT(DISTINCT website_session_id) AS sessions,
	channel_group
FROM (	
	SELECT
		website_session_id,
		created_at,
		CASE
			WHEN utm_source IS NULL AND http_referer IN ('https://www.bsearch.com','https://www.gsearch.com') THEN 'organic_search'
			WHEN utm_campaign = 'nonbrand' THEN 'paid_nonbrand'
			WHEN utm_campaign = 'brand' THEN 'paid_brand'
			WHEN utm_source IS NULL AND http_referer IS NULL THEN 'direct'
		END AS channel_group
	FROM website_sessions
	WHERE created_at < '2012-12-23') AS channel_group
WHERE channel_group IS NOT NULL
GROUP BY 1,2,4;
```
#### Command & Results
```
python3 connect.py --question 6 --db 'mavenfuzzyfactory user password' -task 'run'
```


#### Comments
