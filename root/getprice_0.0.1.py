import requests
import mariadb
import json
from datetime import datetime, timedelta

#업비트 api endpoint&parameter 세팅

url = "https://api.upbit.com/v1/candles/days?market=USDT-BTC&count=200"
symbol = 'KRW-BTC'
interval = 1  # 1 day interval
start_time = (datetime.utcnow() - timedelta(days=200)).strftime('%Y-%m-%d %H:%M:%S')
end_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

conn = mariadb.connect(
    user = 'root',
    password = 'root',
    host = 'localhost',
    port = 3306,
    database = 'PyQuantCOIN'
)

cur = conn.cursor()
#API 요청 보내고 OpenHighLowCloseVolume 데이터 받아오기
response = requests.get(url, params = {'market' : symbol, 'count' :200,'interval' : interval, 'to': end_time, 'from' : start_time })
data = response.json()


#데이터를 마리아디비 데이터베이스에 저장하기
for row in data:
    timestamp = datetime.strptime(row['candle_date_time_kst'], '%Y-%m-%dT %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    cur.execute('INSERT INTO ohlcv (symbol, timestamp, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (symbol, timestamp, row['opening_price'], row['high_price'], row['low_price'], row['trade_price'], row['candle_acc_trade_volume']))
    
conn.commit()
conn.close()