import yfinance as yf
import pandas as pd

# Define the stock tickers
tickers = ['TSLA', 'F', 'GM','ABT','CVS','UNH','NVDA','AMD','AVGO','JPM','C','BRK-B']

# Define the start and end dates
start_date = "2014-07-10"
end_date = "2024-07-10"

# Create an empty DataFrame to store the data
all_data = pd.DataFrame()

# Loop through each ticker and download the data
for ticker in tickers:
    # Download the data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Add a column with the ticker name
    data["Ticker"] = ticker
    
    # Append the data to the all_data DataFrame
    all_data = pd.concat([all_data, data])

# Reset the index to make 'Date' a column
all_data.reset_index(inplace=True)

# Save the data to an Excel file
all_data.to_excel("Historical_Stock_Prices.xlsx", index=False)

print("Data has been downloaded and saved to 'Historical_Stock_Prices.xlsx'")
