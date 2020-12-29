import pandas_datareader.data as pdr 

def get_ticker_quote(ticker):
    data = pdr.get_quote_yahoo(ticker)
    return data 
    
