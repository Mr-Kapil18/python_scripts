import requests
api_key = "OGVCLJ0NLJ3GSM5C"
api_url = "https://www.alphavantage.co/"
symbol = "IBM"
#interval = "5min"
#print(api_url+query)

def get_stock_market_data(symbol):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url=api_url+query)
    #print(response.json())
    for key,Value in response.json().items():
        if key == "Meta Data":
           # continue
        #else:
            print(key,Value)
symbol = input("enter the symbol u want: ")
get_stock_market_data(symbol)
