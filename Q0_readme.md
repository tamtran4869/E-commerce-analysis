### Traffic source analysis - Question 0

#### Task

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

#### Conclusions
The traffic from Google search with non-brand keywords are the main source compared to other sources. We should investigate more this to find whether it could get better.
