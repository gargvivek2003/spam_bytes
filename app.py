# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import requests
import wget

app = Dash(__name__)

apikey = 'Your API Key'
location = '/Users/adity/Desktop/hackathon'

def dailyAdj(symbol, outputsize="compact", datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + \
        symbol + '&outputsize=' + outputsize + \
        '&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)

def fetch(symbol):
    dailyAdj(symbol)
    source = 'daily_adjusted_' + symbol + '.csv'
    df = pd.read_csv(source)
    return df

df = fetch('AAPL')

fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

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
