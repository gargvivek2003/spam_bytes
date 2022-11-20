import requests


def exchange_rate(fr,to):
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + fr + '&to_currency=' +to + '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']
    print(data)
exchange_rate('USD','INR')
