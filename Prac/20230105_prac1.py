import pyupbit as upbit


print(upbit.get_current_price("USDT-BTC"))
a = upbit.get_current_price("USDT-BTC")

print(type(a))
df = upbit.get_ohlcv("USDT-BTC")
print(df.tail())