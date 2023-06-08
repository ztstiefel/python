# This script takes a directory with .csv files inside it, and imports them to a postgresql server. 
# The tables must already have been created in advance, with appropriate column data types.
# The .csv files are assumed to already have been cleaned and ready for import

#TODO: rewrite this code to utilize credentials in a .env file for security
# define imports
import psycopg2, os

# directory below is where the .csv files are located
dir = 'C:\\Users\\<USER>\\<DIRECTORY>' # an example directory - change as needed

# change directory
os.chdir(dir)

# define server connection. Host, username, and password have been redacted.
conn = psycopg2.connect('host=##.#.#.## port=5432 dbname=<DB_NAME> user=<USER> password=<PASSWORD>')
cur = conn.cursor()

# SQL code to be called by copy_expert
sql = "COPY casestudy01 (ride_id,rideable_type,started_at,ended_at,start_station_name,start_station_id,end_station_name,end_station_id,start_lat,start_lng,end_lat,end_lng,member_casual) FROM STDIN DELIMITER ',' CSV"

# Where the magic happens
for file in os.listdir(dir):
    f = os.path.join(dir, file)
    if os.path.isfile(f):
        with open(f, 'r') as f:
            next(f)
            cur.copy_expert(sql, f)
        conn.commit()

# code below removed -redundant
#conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
