### Traffic source analysis - Question 2

#### Task

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


#### Conclusions
The number of sessions go down significantly; hence, the source could be sensitive with bidding price.
