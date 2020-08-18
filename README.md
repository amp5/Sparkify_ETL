# Sparkify_ETL
## Sparkify ETL Pipeline

### Background

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. This project creates an ETL pipeline for Sparkify that combines different datasets stored in a multitude of files and stores them in a database for analysts to easily query the data to find insight. 

### Database Schema Design:

Below are the following tables analysts have access to:
- artists - information on artists such as their name, a unique artist id, their location and latitude and longitude data if available
- users - information on the user's first and last name, a unique id, their gender and whether they have a paid or free account
- time - information on when a user listened to a song such as the starttime and broken down into what hour, day, week, month, year and week of year
- songs - information on song titles, a unique song id, an artist id, the year the song was release and how long the song was for
- song_play - information on when a user played a song, what song, what artist, what user and what session and location user was on

This ETL pipeline uilized a star schema to optimize and simplify quieries which will often be aggregation quieries.  

### Use Cases:
1. Top 10 songs listened to of all time
select s.title, count(*) as num_played from song_play  as sp join songs as s ON sp.song_id = s.song_id group by s.title

2. Distribution between paid and free users
 SELECT level, COUNT(*) FROM users GROUP BY level


### Instructions to run:
- Ensure you have access to PostgreSQL either locally or in the cloud
- clone github repo
- open cloned repo in terminal
- run 'create_tables.py' which creates all of the tables you will need
- run 'etl.py' which inserts all of the data into your tables
- From there run various queries off of your PostgreSQL database using either a python driver or a GUI like PGAdmin

