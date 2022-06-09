import numpy as np
import pandas as pd
import bitso
#import pandas_ta as pta
#12:44 inicio
##################
API_KEY=''
API_SECRET=''
api = bitso.Api(API_KEY,API_SECRET)

#Libros de trade disponibles
exc=[]
books = api.available_books()
for i in books.books:
    if('_usd' in i):
        exc.append(i)

salida=[]
for i in exc:
    tick = api.ticker(i)
    print(i,tick.volume*tick.last)
    salida.append([i,tick.volume*tick.last])

res=pd.DataFrame(salida,columns=["major_minor","volume minor"]).sort_values(by="volume minor",ascending=False)
res_f=res[res["volume minor"]>20000]
print(res_f)
print(len(res_f))

