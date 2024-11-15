import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
prices = [150, 155, 160, 158, 162]

plt.plot(days, prices,color='b')
plt.title('Stock Prices Over 5 Days')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
data = yf.download('GOOGL', start='2023-01-01', end='2023-03-01')
data['Close'].plot(title="Alphabet Inc. Stock Prices", xlabel='Date', ylabel='Price', figsize=(10,6))
plt.show()
