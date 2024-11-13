import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
data = yf.download('GOOGL', start='2023-01-01', end='2023-10-01')
sample_data = data[['Volume']].head(6)
sample_data.plot(kind='bar', title="Alphabet Inc. Trading Volume", xlabel='Date', ylabel='Volume', figsize=(10,6))
plt.show()
