import requests
api_key = "DZ6F26G7XK1HDDIG"


def intra_day()
def daily()
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=' + api_key
    r = requests.get(url)
    data = r.json()
    print(data)
