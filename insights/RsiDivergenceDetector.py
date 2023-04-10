import talib
import ccxt
import time

# Initialize exchange client
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
    'enableRateLimit': True,
})

# Define function to check for bullish and bearish divergences
def check_divergence(symbol):
    # Define time frame and indicator parameters
    timeframe = '4h'
    rsi_period = 14
    upper_threshold = 70
    lower_threshold = 30

    # Get OHLCV data from exchange
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

    # Extract close prices
    close_prices = [float(x[4]) for x in ohlcv]

    # Calculate RSI
    rsi = talib.RSI(close_prices, rsi_period)

    # Check for bullish divergence
    if rsi[-1] < rsi[-2] and close_prices[-1] > close_prices[-2] and rsi[-1] < lower_threshold:
        return "Bullish Divergence detected on " + symbol + " " + timeframe

    # Check for bearish divergence
    elif rsi[-1] > rsi[-2] and close_prices[-1] < close_prices[-2] and rsi[-1] > upper_threshold:
        return "Bearish Divergence detected on " + symbol + " " + timeframe

    # Return None if no divergence is detected
    else:
        return None

# Define main function to run the script
def main():
    while True:
        # Define symbols to check for divergences
        symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'ADA/USDT', 'DOGE/USDT']

        # Check for divergences on each symbol
        for symbol in symbols:
            divergence = check_divergence(symbol)
            if divergence is not None:
                print(divergence)

        # Wait for 15 minutes before checking again
        time.sleep(900)

if __name__ == '__main__':
    main()