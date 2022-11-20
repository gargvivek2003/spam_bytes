# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import requests
import wget

app = Dash(__name__)

apikey = 'YOUR API KEY'
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

def wma(symbol, datatype="csv"):
    url = 'https://www.alphavantage.co/query?function=WMA&symbol=' + \
        symbol + '&interval=weekly&time_period=10&series_type=open&apikey=' + apikey + '&datatype=' + datatype
    wget.download(url, location)

def fetchwma(symbol):
    wma(symbol)
    source = 'technical_indicator_' + symbol + '.csv'
    df2 = pd.read_csv(source)
    return df2

def news(symbol):
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=' + symbol + '&topics=technology&apikey=' + apikey
    r = requests.get(url)
    data = r.json()["feed"]
    new=dict()
    for i in range(0,len(data)):
        new[data[i]["title"]]=data[i]["url"]
    return new

app.layout = html.Div(children=[
    html.H1(children='Stock Market Tickers'),

    html.Div(children='''
        Enter a valid stock symbol to see its data
    '''),

    dcc.Input(id='input-1-state', type='text', value='AAPL'),
    html.Button(id='submit-button-state', n_clicks=0, children='Search'),
    dcc.Graph( id='output-state'),
    dcc.Graph( id = 'output-state-2'),
    dcc.Graph( id = 'output-state-3')
])

@app.callback(Output('output-state', 'figure'),
              Output('output-state-2', 'figure'),
              Output('output-state-3', 'figure'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'))
def update_output( n_clicks, value):
    df = fetch(value)
    df2 = fetchwma(value)
    fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])],)
    fig2 = px.line(df, x = 'timestamp', y = 'open', title = 'Opening Values')
    fig3 = px.line(df2, x = 'time', y = 'WMA', title = 'Weighted Moving Average')
    return fig, fig2 ,fig3 
    

if __name__ == '__main__':
    app.run_server(debug=True)
