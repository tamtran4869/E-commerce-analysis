# Time series analysis
Looking at performance of business by time to determine the pattern. It could use for seasonal analysis and user online behavior analysis. 

## Question 10

Take a look at 2012’s monthly and weekly volume patterns by session volume and order volume.

_Received date: Jan 02, 2013_

#### SQL query 
```
SELECT 
	MONTH(ws.created_at) AS month,
	COUNT(DISTINCT ws.website_session_id) AS sessions,
	COUNT(DISTINCT o.order_id) AS orders,
	COUNT(DISTINCT o.order_id)/COUNT(DISTINCT ws.website_session_id) AS conv_rate
FROM website_sessions ws
LEFT JOIN orders o
	ON ws.website_session_id = o.website_session_id
WHERE ws.created_at <'2013-01-01'
GROUP BY 1;

```
#### Command & Results
```
python3 connect.py --question 10 --db 'mavenfuzzyfactory user password' -task 'run'
```
![image](https://user-images.githubusercontent.com/114192113/211798519-08c4e915-9027-472f-a7ba-d1c2c8a6e698.png)
![image](https://user-images.githubusercontent.com/114192113/211798512-67b8d0f1-7330-41bb-ab67-1c2f90f45081.png)
#### Comments
Overall, all metrics tend to increase during last 3 months, especially sessions in Nov. The reasons could be the rise of demands in holiday season and effective optimisation in marketing and website.
Besides, the conversion chart shows a clear increase trend. Although, Dec is not the month with the hisghest sessions and orders
but it is the highest conversion rate. It proves the good work of the team in optimization.

In my opinion, for further conclusions about seasonality (e.g month or week), the more data is needed.

## Question 11

Analyze the average website session volume, by hour of day and by day week and avoid the 
holiday time period and use a date range of Sep 15 - Nov 15, 2012.

_Received date: Jan 02, 2013_

#### SQL query 
```
SELECT 
	MONTH(ws.created_at) AS month,
	COUNT(DISTINCT ws.website_session_id) AS sessions,
	COUNT(DISTINCT o.order_id) AS orders,
	COUNT(DISTINCT o.order_id)/COUNT(DISTINCT ws.website_session_id) AS conv_rate
FROM website_sessions ws
LEFT JOIN orders o
	ON ws.website_session_id = o.website_session_id
WHERE ws.created_at <'2013-01-01'
GROUP BY 1;

```
#### Command & Results
```
python3 connect.py --question 10 --db 'mavenfuzzyfactory user password' -task 'run'
```
![image](https://user-images.githubusercontent.com/114192113/211798519-08c4e915-9027-472f-a7ba-d1c2c8a6e698.png)
![image](https://user-images.githubusercontent.com/114192113/211798512-67b8d0f1-7330-41bb-ab67-1c2f90f45081.png)
#### Comments
Overall, all metrics tend to increase during last 3 months, especially sessions in Nov. The reasons could be the rise of demands in holiday season and effective optimisation in marketing and website.
Besides, the conversion chart shows a clear increase trend. Although, Dec is not the month with the hisghest sessions and orders
but it is the highest conversion rate. It proves the good work of the team in optimization.

In my opinion, for further conclusions about seasonality (e.g month or week), the more data is needed.
