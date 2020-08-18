# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS song_play;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS song_play (
                                songplay_id varchar PRIMARY KEY, 
                                start_time timestamp, 
                                user_id varchar NOT NULL, 
                                song_id varchar, 
                                artist_id varchar, 
                                session_id varchar,
                                location varchar(200)
                                )
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (
                            user_id int PRIMARY KEY, 
                            first_name varchar(50),
                            last_name varchar(50),
                            gender varchar(50),
                            level varchar(20)
                            )
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs(
                            song_id varchar PRIMARY KEY,
                            title varchar(100),
                            artist_id varchar NOT NULL, 
                            year int, 
                            duration numeric
                            )
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists(
                                artist_id varchar PRIMARY KEY, 
                                name varchar(100),
                                location varchar(200),
                                latitude varchar(100),
                                longitude varchar(100)
                                )
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time(
                            start_time timestamp PRIMARY KEY,
                            hour int, 
                            day int, 
                            week int, 
                            month int,
                            year int,
                            weekday varchar
    )
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO song_play(
                                songplay_id, 
                                start_time, 
                                user_id, 
                                song_id, 
                                artist_id, 
                                session_id,
                                location 
                                )
                                Values(%s, %s, %s, %s, %s, %s, %s)
                                ON CONFLICT DO NOTHING
""")

user_table_insert = (""" INSERT INTO users(
                            user_id, 
                            first_name,
                            last_name,
                            gender,
                            level 
                            )
                            Values(%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")

song_table_insert = (""" INSERT INTO songs (
                            song_id, 
                            title, 
                            artist_id, 
                            year, 
                            duration)
                            Values (%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")

artist_table_insert = (""" INSERT INTO  artists (
                            artist_id, 
                            name, 
                            location,
                            latitude,
                            longitude)
                            Values (%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")

time_table_insert = (""" INSERT INTO time(
                            start_time,
                            hour, 
                            day, 
                            week, 
                            month,
                            year
                            )
                            Values(%s, %s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")
# FIND SONGS

song_select = (""" SELECT s.song_id, s.artist_id
                    FROM songs as s
                    JOIN artists as a ON s.artist_id = a.artist_id
                    WHERE s.title = %s 
                        AND a.name = %s
                        AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]