import pandas_datareader.data as web
import datetime

print('Enter ticker: ')
ticker = input()

end_date = datetime.date.today()
start_date=end_date.replace(year=end_date.year-1)

historical_prices = web.DataReader(ticker, data_source='yahoo',start=start_date,end=end_date)
print(historical_prices)