#code to fetch stock market information
import wget
location = 'D:\JIIT MATERIAL\3rd Sem\Hackathon'

# todo Time Series

def daily(symbol, outputsize="compact", datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        symbol + '&outputsize=' + outputsize + \
        '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def dailyAdj(symbol, outputsize="compact", datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + \
        symbol + '&outputsize=' + outputsize + \
        '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def intraday(symbol, interval, outputsize="compact", datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + \
        '&interval=' + interval + '&outputsize=' + outputsize + \
        '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def weekly(symbol, datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + \
        symbol + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def weeklyAdj(symbol, datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=' + \
        symbol + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def monthly(symbol, datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + \
        symbol + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def monthlyAdj(symbol, datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=' + \
        symbol + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)

# todo Fundamental Data


def overview(symbol):
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + \
        symbol + '&apikey=' + apikey
    wget.download(url, location)


def income(symbol):
    url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + \
        symbol + '&apikey=' + apikey
    wget.download(url, location)


def balancesheet(symbol):
    url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + \
        symbol + '&apikey=' + apikey
    wget.download(url, location)


def cashflow(symbol):
    url = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + \
        symbol + '&apikey=' + apikey
    wget.download(url, location)

# todo Forex
# I had to use from as form due to from being a reserved word


def exchangerate(form, to):
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE' + \
        '&from_currency=' + form + '&to_currency=' + to + '&apikey=' + apikey
    wget.download(url, location)


def intradayFX(form, to, interval, outputsize='compact', datatype='json'):
    url = 'https://www.alphavantage.co/query?function=FX_INTRADAY' + '&from_symbol=' + form + '&to_symbol=' + \
        to + '&interval=' + interval + '&outputsize=' + \
        outputsize + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def dailyFX(form, to, outputsize='compact', datatype='json'):
    url = 'https://www.alphavantage.co/query?function=FX_DAILY' + '&from_symbol=' + form + \
        '&to_symbol=' + to + '&outputsize=' + outputsize + \
        '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def weeklyFX(form, to, datatype='json'):
    url = 'https://www.alphavantage.co/query?function=FX_WEEKLY' + '&from_symbol=' + \
        form + '&to_symbol=' + to + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def monthlyFX(form, to, datatype='json'):
    url = 'https://www.alphavantage.co/query?function=FX_MONTHLY' + '&from_symbol=' + \
        form + '&to_symbol=' + to + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)

# todo Crypto


def dailyCrypto(symbol, market, datatype='json'):
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY' + '&symbol=' + \
        symbol + '&market=' + market + '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def weeklyCrypto(symbol, market, datatype='json'):
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY' + \
        '&symbol=' + symbol + '&market=' + market + \
        '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def monthlyCrypto(symbol, market, datatype='json'):
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY' + \
        '&symbol=' + symbol + '&market=' + market + \
        '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)


def cryptoRating(symbol):
    url = 'https://www.alphavantage.co/query?function=CRYPTO_RATING' + \
        '&symbol=' + symbol + '&apikey=' + apikey
    wget.download(url, location)

