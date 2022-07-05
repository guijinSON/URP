import yfinance as yf
import pandas as pd
equity = pd.read_excel('(N=30)Equity List-GSON.xlsx')

data = yf.download( 
        tickers = ' '.join(equity['Symbols'].values),
        start='2010-01-01',
        end='2021-12-31',
        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

data.to_excel('(N=30 | Freq=1D) Historical Data-GSON.xlsx')
