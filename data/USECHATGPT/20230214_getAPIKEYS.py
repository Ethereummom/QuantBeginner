import requests
import pandas as pds

endpoint = 'https://api.binance.com/api/v3/klines'

params = {
    'symbol' : 'BTCUSDT',
    'interval' : '1d',
    'limit' : 365
}

response = requests.get(endpoint,params = params)
data = response.json()

df = pds.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
df['timestamp'] = pds.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp',inplace = True)

print(df.head())