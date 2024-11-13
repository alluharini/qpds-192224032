import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
data = yf.download('GOOGL', start='2023-01-01', end='2023-03-01')
data['Close'].plot(title="Alphabet Inc. Stock Prices", xlabel='Date', ylabel='Price', figsize=(10,6))
plt.show()
