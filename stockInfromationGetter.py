# get stock information:
## stock symbol, price, date
import requests


def stockGetter(symbol_list:list) -> dict:
    """"
    sample input: ['APPL']
    sample output:
    'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', 
    '2. Symbol': 'IBM', 
    '3. Last Refreshed': '2021-12-03', 
    '4. Output Size': 'Compact', 
    '5. Time Zone': 'US/Eastern'}, 
    'Time Series (Daily)':{**data}
    """
    stocks_data_dict = {}
    for symbol in symbol_list:
        # call the api for each symbol
        #try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=ICAGTOFCYS3PIDU0'
        r = requests.get(url)
        #except err as e:
        stocks_data_dict.update(r.json())
    return stocks_data_dict

#stockGetter(['AAPL','TSLA'])

# for reading excel files, look into pandas.read_excel(sheets/sheet_name = )

def userDataAssembler() -> dict:
    """ 
      returned dictionary should contain below information
    - user_name
    - symbol
    - price_bought_in (mark to do)
    - shares
    - bought-in value total"""
    user_name = input('type your user name')
    _symbol_list = input('please input your stock symbols you wish to purchase ,seperated by comma (e.g)') # 
    symbol_list = _symbol_list.split(',')
    user_purchase_order = {}
    
    for symbol in symbol_list:
        while True:
            try:
                shares = input(f'for {symbol}, how many shares you want to purchase? (e.g. 1')
                # use getstock to get price
                price = #doyourthing
                user_purchase_order.update({user_name:{symbol:shares, symbol:price}})
                # homework 2.2 calculate the total of value by price X share
                break
            except Exception: # Try to catch something more specific
                pass

    # create the data format that we want to insert into the database -> list of insert statement(str)
    # hint: get today's date - from datetime import date / date.now().stftime() ; you could format the date to be synced with your own date format (%m-%d-%Y)
    # delete user data: DELETE From stocks where user_name = {user_name} and date = {today} and stock = {symbol};
    return [f"INSERT INTO stocks VALUES ({user_name},'AAPL','10', '120', '1200', '12-10-2021')",
    f"INSERT INTO stocks VALUES ({user_name},'TSLA','10', '120', '1200', '12-10-2021')"]

    return user_purchase_order
        # validation on the shares input 
        
    

    # homework 2.1 use the stockGetter to get the most recent price as the - price_bought_in (mark to do) value
   
    # homework 2.3 create user_purchase_data dict based on info above

    #return user_purchase_data


def verify(user_purchase_order):
    for 