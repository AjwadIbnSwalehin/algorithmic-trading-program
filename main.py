import yfinance as yf
import matplotlib.pyplot as plt

start_date = "2020-01-01"
end_date = "2023-01-01"

msft = yf.download("MSFT", start_date, end_date, group_by="ticker")

sma_200 = msft["Close"].rolling(200, center=True).mean()
sma_50 = msft["Close"].rolling(50, center=True).mean()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(sma_200, color="red", label="SMA 200")
ax.plot(sma_50, color="green", label="SMA 50")

ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('MSFT Stock Price with Simple Moving Average')

for i in range(len(msft)):
    if sma_200[i - 1] <= sma_50[i - 1] and sma_200[i] > sma_50[i]:
        ax.scatter(sma_200.index[i], sma_200[i], marker="o", color="red", s=50)
    elif sma_200[i - 1] >= sma_50[i - 1] and sma_200[i] < sma_50[i]:
        ax.scatter(sma_50.index[i], sma_50[i], marker="o", color="green", s=50)

plt.xticks(rotation=45)
plt.show()
