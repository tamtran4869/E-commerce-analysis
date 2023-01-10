### Traffic source analysis - Question 1

#### Task

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

#### Conclusions
It is clear that the conversion rate of Google search - nonbrand source does not meet the requirement.  
