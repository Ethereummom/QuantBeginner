import requests
import json
import mariadb
from datetime import datetime, timedelta

# Define the Upbit API endpoint and parameters
url = 'https://api.upbit.com/v1/candles/days'
market = 'KRW-BTC'
count = 30  # retrieve the last 30 days of data

# Define the MariaDB connection parameters
host = 'localhost'
port = 3306
user = 'root'
password = 'root'
database = 'PyQuantCOIN'

# Connect to the MariaDB database
conn = mariadb.connect(
    user='root',
    password='root',
    host='localhost',
    port=3306,
    database='PyQuantCOIN'
)
cur = conn.cursor()

# Retrieve the candle data from the Upbit API
params = {'market': market, 'count': count}
response = requests.get(url, params=params)
data = json.loads(response.content)


# Insert the candle data into the MariaDB database
for row in data:
    timestamp = int(row['candle_date_time_utc'].replace('T', '')[:-8])
    utc_date = datetime.utcfromtimestamp(timestamp)
    kst_date = utc_date + timedelta(hours=9)
    cur.execute(
        "INSERT INTO daily_candles (symbol, date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (market, kst_date.date(), row['opening_price'], row['high_price'], row['low_price'], row['trade_price'], row['candle_acc_trade_volume'])
    )
    conn.commit()

# Close the database connection
cur.close()
conn.close()