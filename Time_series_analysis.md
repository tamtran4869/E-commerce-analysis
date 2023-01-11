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

![image](https://user-images.githubusercontent.com/114192113/211801859-a49b343e-768c-4695-8ffa-28e9caebea7a.png)

#### Comments
Overall, all metrics tend to increase during last 3 months, especially sessions in Nov. The reasons could be the rise of demands in holiday season and effective optimisation in marketing and website.
Besides, the conversion chart shows a clear increase trend. Although, Dec is not the month with the hisghest sessions and orders
but it is the highest conversion rate. It proves the good work of the team in optimization.

In my opinion, for further conclusions about seasonality (e.g month or week), the more data is needed.

## Question 11

Analyze the average website session volume, by hour of day and by day week and avoid the 
holiday time period and use a date range of Sep 15 - Nov 15, 2012.

_Received date: Jan 05, 2013_

#### SQL query 
```
SELECT
	hour,
	AVG(CASE WHEN weekday = 0 THEN sessions ELSE NULL END) AS mon,
	AVG(CASE WHEN weekday = 1 THEN sessions ELSE NULL END) AS tue,
	AVG(CASE WHEN weekday = 2 THEN sessions ELSE NULL END) AS wed,
	AVG(CASE WHEN weekday = 3 THEN sessions ELSE NULL END) AS thu,
	AVG(CASE WHEN weekday = 4 THEN sessions ELSE NULL END) AS fri,
	AVG(CASE WHEN weekday = 5 THEN sessions ELSE NULL END) AS sat,
	AVG(CASE WHEN weekday = 6 THEN sessions ELSE NULL END) AS sun
FROM 
	(
	SELECT
		DATE(created_at) AS created_date,
		WEEKDAY(created_at) AS weekday,
		HOUR(created_at) AS hour,
		COUNT(DISTINCT website_session_id) AS sessions
	FROM website_sessions
	WHERE created_at >= '2012-09-15' AND created_at <='2012-11-15'
	GROUP BY 1,2,3
	) AS daily_sessions
GROUP BY hour
ORDER BY hour;

```
#### Command & Results
```
python3 connect.py --question 11 --db 'mavenfuzzyfactory user password' -task 'run'
```
![image](https://user-images.githubusercontent.com/114192113/211802817-d869d2d3-63df-4b29-86cd-c1e901160195.png)

A heatmap is a great choice to visual this type of data.

![image](https://user-images.githubusercontent.com/114192113/211802855-04baf0d4-ca43-496f-bac2-acbb35bd5f48.png)

#### Comments

Sessions focus on Monday to Friday during office time (8-17), especially Wednesday with 2 peaks at 11 and 15. From this insight, the marketing team could set up time targeting reasonable and the support team could plan staff schedule to deal with high volumns.

It is interested that the heatmap looks like behavior of B2B. It could be the desktop-device targeting of marketing campaigns and a huge demand from B2B clients. Following 2 hypothesises, the team could try to target mobile device on weekend and off hours; the company could investigate more the B2B sections.
