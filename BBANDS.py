import pandas as pd
import talib

df = pd.read_excel('(N=30 | Freq=1D) Historical Data-GSON.xlsx')

symbol = 'F'
input_val = data[f'{symbol}']['Close'].values
upper, middle, lower = talib.BBANDS(input_val, matype=talib.MA_Type.T3)

plt.plot(input_val)
plt.plot(upper)
plt.plot(middle)
plt.plot(lower)
