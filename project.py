import numpy as np
import pandas as pd
import requests 
import json
from bs4 import BeautifulSoup

url="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
result= pd.read_html(url)
table = result[3]
table.columns=range(table.shape[1])
#print(table)#antes
table=table[[0,2]]
table=table.iloc[0:10,:]
table.columns=["Country", "GDP"]
print("***************************************************************")
print("***********************CON PANDAS******************************")
print("***************************************************************")
print(table)



print("***************************************************************")
print("***********************CON BEAUTIFULSOUP************************")
print("***************************************************************")

def search_table(info, tables):
    found_table=None
    for table in tables:
        if info in table.text:
            found_table=table
            break
                
    return found_table

r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
tables=soup.find_all('table')
table2=search_table('GDP (USD million) by country', tables)
data=[]
if table2:
    for tr in table2.find_all('tr')[2:]:
        data.append(tr.text.split('\n'))
    df=pd.DataFrame(data)
    df=df[[1,3]]
    df.columns=["Country","GDP" ]
    print(df[0:10])
   # df.to_excel("Info Wiki.xlsx")
else:
    print("fallo")