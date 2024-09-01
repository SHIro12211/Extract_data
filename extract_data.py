import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def make_graph(stock_data, revenue_data, stock):
    """
    Parameters:dataframe, dataframe, name of the stock
    """
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

aapl=yf.Ticker('TSLA')
#creo un objeto TICKER
tesla_data = aapl.history(period="max")#devulve un dataframe
tesla_data=tesla_data.reset_index()[:5]
print(tesla_data)
#Using Webscraping to Extract Tesla Revenue Data
html_data= requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm").text
soup=BeautifulSoup(html_data, "html.parser")
tesla_revenue=pd.DataFrame(columns=['Date', 'Revenue'])
for table in soup.find_all("table"):#buscar la tabla correcta
    if "Tesla Quarterly Revenue" in table.text:
        for row in table.find("tbody").find_all('tr'):#recorrer todas sus filas
            col=row.find_all('td')
            date=col[0].text
            revenue=col[1].text
            tesla_revenue=pd.concat([tesla_revenue, pd.DataFrame({'Date':[date], 'Revenue':[revenue]})], ignore_index=True)

print("****************antes************")
print(tesla_revenue.head())
#LIMPIEZA DE DATOS
#para remover el signo de dolar y comas de la columna revenue
tesla_revenue["Revenue"]=tesla_revenue["Revenue"].str.replace(',|\$', "", regex=True)

#para remover las lineas null o string en blanco en la columna revenue
tesla_revenue=tesla_revenue[tesla_revenue['Revenue']!=""]
print("****************despues*********************")
print(tesla_revenue.head())
make_graph(tesla_data, tesla_revenue, 'Tesla')
