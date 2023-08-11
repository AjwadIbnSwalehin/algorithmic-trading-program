import alpaca_trade_api as tradeapi
import os
import yfinance as yf

# Set up the Alpaca API client: API keys are hidden
api = tradeapi.REST(os.getenv("alpaca_key"), os.getenv(
    "alpaca_secret"), base_url='https://paper-api.alpaca.markets')

# Get the data for MSFT from the Alpaca API
symbol = 'MSFT'
start_date = '2020-01-01'
end_date = '2023-01-01'

msft = yf.download("MSFT", start_date, end_date, group_by="ticker")

sma_200 = msft["Close"].rolling(200, center=True).mean()
sma_50 = msft["Close"].rolling(50, center=True).mean()

# Define the number of shares to buy and sell
num_shares = 1

portfolio = api.list_positions()

if len(portfolio) == 0:
    api.submit_order(
        symbol=symbol,
        qty=num_shares,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

# Loop through the data and implement your trading strategy
for i in range(len(msft)):
    # Check if it's time to buy or sell
    if sma_200[i - 1] <= sma_50[i - 1] and sma_200[i] > sma_50[i]:
        api.submit_order(
            symbol=symbol,
            qty=num_shares,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    elif sma_200[i - 1] >= sma_50[i - 1] and sma_200[i] < sma_50[i]:
        api.submit_order(
            symbol=symbol,
            qty=num_shares,
            side='sell',
            type='market',
        )
