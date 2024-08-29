import requests
from  bs4 import BeautifulSoup
import pandas as pd

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#Send an HTTP request to the web page using the requests library.
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
request = requests.get(URL).text
#Parse the HTML content of the web page using BeautifulSoup.
soup= BeautifulSoup(request, "html.parser")
#Identify the HTML tags that contain the data you want to extract.
netflix_data=pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

#Identify the HTML tags that contain the data you want to extract.
for row in soup.find('tbody').find_all('tr'):#lista de rows
    col= row.find_all('td')
    date= col[0].text
    open= col[1].text
    high= col[2].text
    low= col[3].text
    close= col[4].text
    adj_close = col[5].text
    volumen= col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volumen]})], ignore_index=True)    
    #el metodo concat es para añadir una una fila al dataframe
print(netflix_data.head())
#head devuelve lass 5 primeras filas del dataframe
#*********************************************************************************


   