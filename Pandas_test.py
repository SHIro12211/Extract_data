
import pandas as pd

xls_path="resource/List-of-customers-with-name-and-address.xls"
df = pd.read_excel(xls_path)
#necesite instalar 'pip install xlrd' y 'pip install'
df_name=df[['Name']]
df_name1=df['Name']
print(type(df_name))#:pandas.core.frame.DataFrame
print(type(df_name1))#:pandas.core.series.Series

print(df.iloc[0:10,0:5])
print(df.loc[0:10, 'Name':"Address"])
print("***********************************************************************************************")
print("***********************************************************************************************")
df_test=df.loc[0:10, "Name":"Address"]
df_test=df_test.set_index("Name")
print(df_test)
print(df_test.iloc[:5])

