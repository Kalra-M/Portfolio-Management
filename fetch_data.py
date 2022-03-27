import yfinance as yf

#Symbols of stocks as give on YahooFinance
stocks = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFC.NS', 'TATAMOTORS.NS', 'SUNPHARMA.NS', 'ONGC.NS', 'HINDUNILVR.NS', 'MARUTI.NS', 'TATASTEEL.NS']

#Download for the month of January
df = yf.download(' '.join(stocks), start = '2022-01-01', end = '2022-02-01')
  
#Save
df['Close'].to_excel('NSE_10_January.xlsx', 'Raw')