import yfinance as yf
import pandas as pd

# read the file with stock symbols
variables = pd.read_csv("companies.csv")

# difference between the previous 5 days avg volume and today's volume
volume_difference = 2

# extract the symbols
symbols = variables['Symbol']

#print("SYMBOL\t\tPREVIOUS AVERAGE\t\tTODAY VOLUME")

print("{0:<20} {1:<25} {2:<20} {3:<10}".format("SYMBOL", "PREVIOUS AVERAGE", "VOLUME TODAY", "DIFFERENCE"))
for stock in symbols:
    stock = stock.upper()
    if '^' in stock:
        pass
    else:
        try:
            # get the stock data from yahoo finance
            stock_info = yf.Ticker(stock)

            # get the history for the last 5 days
            hist = stock_info.history(period="5d")

            # calculate the mean for the last 5 days volume
            previous_averaged_volume = hist['Volume'].iloc[1:4:1].mean()

            # extract today's volume
            todays_volume = hist['Volume'][-1]

            # extract the previous day close volume
            previous_close = hist['Close'][-2]

            # extract the current day close volume
            current_close = hist['Close'][-1]

            # check if there is a difference between the today volume compared to the last 5 days average
            if todays_volume > previous_averaged_volume * volume_difference and previous_close < current_close and todays_volume > 100000:
                
                difference = todays_volume / previous_averaged_volume
                
                print("{0:<20} {1:<25} {2:<20} {3:<10}".format(stock, previous_averaged_volume, todays_volume, str(difference)))
                #print(stock)
                #print(previous_averaged_volume)
                #print(todays_volume)
                
        except:
            pass