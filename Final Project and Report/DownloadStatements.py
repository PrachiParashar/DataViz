import yfinance as yf
import pandas as pd

# Define the tickers for Tesla, Ford, and General Motors
tickers = ['TSLA', 'F', 'GM','ABT','CVS','UNH','NVDA','AMD','AVGO','JPM','C','BRK-B']

# Initialize an empty DataFrame to store all financial data
all_data = pd.DataFrame()

# Function to fetch financial data and append to the DataFrame
def fetch_financial_data(ticker):
    # Fetch the stock data
    stock = yf.Ticker(ticker)
    
    # Get the stock price
    stock_price = stock.history(period="1d")['Close'].iloc[0]
    
    # Get the income statement, balance sheet, and cash flow
    income_statement = stock.financials.T
    balance_sheet = stock.balance_sheet.T
    cash_flow = stock.cashflow.T
    
    # Add columns for the report type and stock price
    income_statement['Report Type'] = 'Income Statement'
    balance_sheet['Report Type'] = 'Balance Sheet'
    cash_flow['Report Type'] = 'Cash Flow'
    
    income_statement['Current Stock Price'] = stock_price
    balance_sheet['Current Stock Price'] = stock_price
    cash_flow['Current Stock Price'] = stock_price
    
    # Add a column for the ticker symbol
    income_statement['Ticker'] = ticker
    balance_sheet['Ticker'] = ticker
    cash_flow['Ticker'] = ticker
    
    # Append the data to the all_data DataFrame
    return pd.concat([income_statement, balance_sheet, cash_flow])

# Loop through each ticker and fetch the data
for ticker in tickers:
    all_data = pd.concat([all_data, fetch_financial_data(ticker)])

# Reset the index to have a clean DataFrame
all_data.reset_index(inplace=True)

# Save the DataFrame to an Excel file
all_data.to_excel("financial_data.xlsx", index=False)
