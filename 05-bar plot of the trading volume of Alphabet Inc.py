import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
prices = [150, 155, 160, 158, 162]

plt.bar(days, prices,color='b')
plt.title('Stock Prices Over 5 Days')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
data = yf.download('GOOGL', start='2023-01-01', end='2023-10-01')
sample_data = data[['Volume']].head(6)
sample_data.plot(kind='bar', title="Alphabet Inc. Trading Volume", xlabel='Date', ylabel='Volume', figsize=(10,6))
plt.show()
