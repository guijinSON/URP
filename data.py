import yfinance as yf
import pandas as pd

def import_stock_historical(ticker,START='2010-01-01',END='2021-12-31'):
    data = yf.download( 
            tickers = ticker, #' '.join(equity['Symbols'].values),
            start=START,
            end=END,
            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            interval = "1d",
            group_by = 'ticker',
            auto_adjust = True,
            prepost = True,
            threads = True,
            proxy = None
        )
    return data
