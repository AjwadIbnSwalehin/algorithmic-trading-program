# Algorithmic Trading Program
A python script that uses an algorithm to buy and sell stocks for you based on certain requirements. I created this project for my Extended Project Qualification (EPQ)

![image](https://github.com/AjwadIbnSwalehin/algorithmic-trading-program/assets/103510865/418b5a3d-7cc8-4610-ab0c-25f1cff7f443)

## Requirements
You'll need the following to be able to run this
- `yfinance`
- `matplotlib`
- `alpaca_trade_api`

To install the libraries run:
```
pip3 install yfinance
```
Replace yfinance with requests as well.
You will require an API Key to use the Alpaca Trade API, which is an online trading platform.

## Usage
Before running the script, please change the following variables to match the stock that you want to trade
```python
# Change these variables to match your stock, for example, AAPL
msft = yf.download("MSFT", start_date, end_date, group_by="ticker") # main.py
symbol = 'MSFT' # execution.py
```
In order to run the script, open main.py on any Python IDE, and press run.
