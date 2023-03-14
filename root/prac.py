import requests

url = "https://api.upbit.com/v1/candles/days?market=USDT-BTC&count=200"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)