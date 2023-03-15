# This script utilizes the API from https://www.visualcrossing.com to pull  yesterday'sthe weather data for Houston, TX
# TODO:
#   - make database connection more secure
#   - find a way to run script automatically
#   - run script run entirely in memory - no saving a csv file to disk (redundant step)
#   - improve code comments
#   - function @ line 29: use relative path (use sys)
#   - refactor code. Use functions.

import psycopg2, pandas as pd

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/<YOUR_API_KEY_HERE>'
df = pd.read_csv(url)

df.head()

df.to_csv('weather_temp.csv', index=False)

conn = psycopg2.connect('port=5433 dbname=$DB_NAME user=$DB_USER password=$DB_PASSWORD')

cur = conn.cursor()

sql = """ "COPY houston2 (name,datetime,tempmax,tempmin,temp,feelslikemax,feelslikemin,feelslike,
           dew,humidity,precip,precipprob,precipcover,preciptype,snow,snowdepth,
           windgust,windspeed,winddir,sealevelpressure,cloudcover,visibility,
           solarradiation,solarenergy,uvindex,severerisk,sunrise,sunset,moonphase,
           conditions,description,icon,stations) FROM STDIN DELIMITER ',' CSV" """

with open('C:\\YOUR\\FILE\\PATH\\test02x.csv', 'r') as f:
    next(f) #  To Skip the header row.
    cur.copy_expert(sql, f)

conn.commit()

cur.close()

conn.close()