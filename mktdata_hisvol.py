import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime




#Calculating historical prices

ticker='GOOGL'
end_date = datetime.date.today()
start_date=end_date.replace(year=end_date.year-1)

historical_prices = web.DataReader(ticker, data_source='yahoo',start=start_date,end=end_date)

#Save the market data to a csv file
filename=ticker+'_marketdata_asof_'+end_date.strftime('%Y-%m-%d')+'.csv'
print(filename)
export_csv = historical_prices.to_csv (filename, index = None, header=True)
print(historical_prices)




#Calulating historical volatility

#Logarithmic day to day returns
log_returns = np.log(historical_prices['Adj Close'] / historical_prices['Adj Close'].shift(1))

#Standard deviation of returns
df = pd.DataFrame(log_returns)
print(df)
std_returns = df.std()
print(std_returns)

#Annualizing Historical Volatility
historical_vol = std_returns * np.sqrt(252)
print(historical_vol)

data = {'Values':['Standard Deviation of ','Historical Volatility'],'':[std_returns,historical_vol]}
x = pd.DataFrame(data)
print(x)




#Export to excel
writer = pd.ExcelWriter('Python '+ticker+' Market Data & Historical Vol.xlsx', engine = 'xlsxwriter')
export_excel_hispx = historical_prices.to_excel(writer, sheet_name = 'Historical Prices')
export_excel_log_returns = df.to_excel(writer, sheet_name = 'Daily Returns')
export_excel_data = x.to_excel(writer, sheet_name = 'Summary')
writer.save()