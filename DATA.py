import requests
import plotly.express as px
from dash import Dash, html, dcc
import pandas as pd

api_key="YOUR API KEY"

def intra_day():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=' + api_key
    r = requests.get(url)
    data = r.json()
    print(data)

def weekly(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + symbol + '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()["Weekly Time Series"]
    wma(data)

def wma(data):
    key=list(data.keys())
    #st=key[0]
    #date=int(st[-2:])+7
    dic=dict()
    for i in range(0,len(key)-5):
         j=5
         sum=0
         for k in range(1,6):
             sum=sum+j*float(data[key[i+1]]["1. open"])
             j=j-1
         data[key[i]]=float(data[key[i]]["1. open"])
         sum=sum/15
         dic[key[i]]=str(sum)
    app = Dash(__name__)

    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Date": list(dic.keys())[0:1],
        "Values": (list(dic.values()))[0:1],
    })

    fig = px.line(df, x="Date", y="Values")
    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
    if __name__ == '__main__':
        app.run_server(debug=True)

def news(symbol):
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=' + symbol + '&topics=technology&apikey=' + api_key
    r = requests.get(url)
    data = r.json()
    print(data)

#str1=str(input("Enter the symbol of the company : "))
weekly("IBM")
