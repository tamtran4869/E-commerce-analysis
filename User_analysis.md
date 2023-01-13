# User analysis
By understanding different segments of users, the team could know which the main audiences to decide which one
to focus on and plan different marketing, website deisgn and siutable recommendation.

In this case, the segments of new and old users in the website were considered.

## Question 18

Pull data on how many of our website visitors come back for another session from 2014.

_Received date: Nov 01, 2014_

#### SQL query 
There are some steps to get the data:

1. Filter to get new users and their first session id

![image](https://user-images.githubusercontent.com/114192113/212206484-d2467011-d6d8-499a-92f8-70ffc516b743.png)

2. Join the new sessions data with the repeat sessions (filter from the website_sessions table), 
to get the user id, the first session id, and all the next/repeat sessions id. 
NULL in this table means there is no repeat session corespondent to the user_id and new_session_id.

![image](https://user-images.githubusercontent.com/114192113/212206565-f216dd5b-2134-40c9-8ed3-d2264be26a6b.png)

3. Group by user_id to count how many new sessions (always 1) and how many repeat sessions of each user.

![image](https://user-images.githubusercontent.com/114192113/212206608-64e2e064-73e1-4696-b18a-a1d7d68c82f1.png)

4. Group by number of repeat sessions and count users.

![image](https://user-images.githubusercontent.com/114192113/212206678-5a713cfe-bec2-483f-af9a-8f6f8c0663fd.png)

The full query:
```
-- Get users with new and repeat session id
WITH session_new_repeat AS (
SELECT
	ns.user_id,
	ns.website_session_id AS new_session_id,
	ws.website_session_id AS repeat_session_id
FROM (
	SELECT -- Get new session id
		user_id,
		website_session_id
	FROM website_sessions
	WHERE 
		created_at < '2014-11-01'
		AND created_at >= '2014-01-01'
		AND is_repeat_session = 0
	) AS ns
LEFT JOIN website_sessions ws  -- Join with the repeat session id
	ON ws.user_id = ns.user_id
	AND ws.is_repeat_session = 1
	AND ws.website_session_id > ns.website_session_id
	AND ws.created_at < '2014-11-01'
	AND created_at >= '2014-01-01')

-- Group by number of repeat sessions and count users
SELECT
	repeat_sessions,
	COUNT(DISTINCT user_id) AS users
FROM	(
	SELECT -- Count number of new and repeat sessions per user
		user_id,
		COUNT(DISTINCT new_session_id) AS new_sessions,
		COUNT(DISTINCT repeat_session_id) AS repeat_sessions
	FROM session_new_repeat
	GROUP BY user_id
	) AS count_sessions
GROUP BY 1;
```
#### Command & Results

```
python3 connect.py --question 18 --db 'mavenfuzzyfactory user password'
```

![image](https://user-images.githubusercontent.com/114192113/212207131-50a1982a-e055-42dd-a844-16cc715fcd3c.png)

#### Comments

New users played a main role in the website traffics. 
The users with 1 and 3 times in the webiste were significant as well. The maximum of number of repeat sessions was 3.

## Question 19

Get data to understand the minimum, maximum, and average time between the first and second session.

_Received date: Nov 02, 2014_

#### SQL query 
There are 4 steps:

1&2. Step 1 and step 2 were same with Q18, except adding time for new sessions and repeat session and 
using HAVING command to remove all user_id without repeat sessions.

![image](https://user-images.githubusercontent.com/114192113/212207530-c19457e0-e12f-46a2-8a23-b8b8913a9a9b.png)

3. From the table above, keep only the smallest repeat session id and time which means the next session 
after the new session, then group by user_id (e.g. it removed a record of user_id 152849 in the table step 3, 
compared to the table step 2).

![image](https://user-images.githubusercontent.com/114192113/212207661-f98d6dd3-6c12-4bda-b919-7d8ca0d0735d.png)

4. Compute average, min and max days from new sessions to next sessions.

![image](https://user-images.githubusercontent.com/114192113/212207730-b25c877f-2525-487a-b6a2-3dae9f269246.png)

The full query:

```
-- Get users with repeat sessions
WITH session_new_repeat AS (
SELECT
	ns.user_id,
	ns.website_session_id AS new_session_id,
	ns.created_at AS new_session_time,
	ws.website_session_id AS repeat_session_id,
	ws.created_at AS repeat_session_time
FROM (
	SELECT -- Get new session id
		user_id,
		website_session_id,
		created_at
	FROM website_sessions
	WHERE 
		created_at < '2014-11-03'
		AND created_at >= '2014-01-01'
		AND is_repeat_session = 0
	) AS ns
LEFT JOIN website_sessions ws -- Join with the repeat session id 
	ON ws.user_id = ns.user_id
	AND ws.is_repeat_session = 1
	AND ws.website_session_id > ns.website_session_id
	AND ws.created_at < '2014-11-03'
	AND ws.created_at >= '2014-01-01'
HAVING ws.website_session_id IS NOT NULL)

--Compute the statistics of date diff
SELECT 
	AVG(DATEDIFF(next_session_time,new_session_time)) AS avg_days,
	MIN(DATEDIFF(next_session_time,new_session_time)) AS min_days,
	MAX(DATEDIFF(next_session_time,new_session_time)) AS max_days
FROM 	(
	SELECT -- Get the next session id
		user_id,
		new_session_id,
		new_session_time,
		MIN(repeat_session_id) AS next_session_id,
		MIN(repeat_session_time) AS next_session_time
	FROM session_new_repeat
	GROUP BY user_id
	) AS session_new_next;
```
#### Command & results

```
python3 connect.py --question 19 --db 'mavenfuzzyfactory user password'
```
#### Comments
It tooks average around 1 month to users come back to the website.
The team could use the insight to setup time for remarketing 1 month.


