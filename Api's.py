import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


cg=CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
print(bitcoin_data.keys())
df=pd.DataFrame(bitcoin_data['prices'], columns=["TimeStamp", "Price"])
print(df)
df["date"]=pd.to_datetime(df["TimeStamp"], unit="ms")
print(df)
candlestick_data=df.groupby(df.date, as_index=False).agg({'Price':['min', 'max', 'first', 'last']})
print(candlestick_data)

fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'][0:10],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

#fig.show()
print("*********************************************************************************************")
from randomuser import RandomUser
r = RandomUser()
some_list = r.generate_users(10)
print(some_list)
data=[]
for user in some_list:
    data.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
x=pd.DataFrame(data)
print("LLLLLLLLLLLLLLLLLLL")
print(data)

print("*********************************************************************************************")
import json
import requests as r

data = r.get("https://fruityvice.com/api/fruit/all")
result= json.loads(data.text)
df2=pd.json_normalize(result)
#buscar las calorias de la fruta banana
buscar='Banana'
banana=df2.loc[df2["name"] == buscar]
print("La fruta "+buscar+" tiene "+str(banana.iloc[0]["nutritions.calories"])+" calorias")