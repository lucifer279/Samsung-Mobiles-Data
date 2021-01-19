
#Flipkart
#Samsung Phones Below 20000

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib

url = 'https://www.flipkart.com/search?q=samsung+phones+below+20000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

r = requests.get(url,header)

content = r.content
# print(content)

#Using Beautiful Soup

soup = BeautifulSoup(content,'html.parser')  #html5lib / html.parser / lxml

# print(soup)

prettify = soup.prettify()   # To pretiffy soup
# print(prettify)

title = soup.find('title')    # To get title
title_text  = title.text
# print(title_text)


#Product Details

productname = soup.find_all('div',class_ = '_4rR01T')

price = soup.find_all('div',class_ = '_30jeq3 _1_WHN1')

ratings = soup.find_all('span',class_ = '_1lRcqv')

productspec = soup.find_all('ul',class_ = '_1xgFaf')


#Final details with clean list

finalproductname =[]

for i in productname:
    finalproductname.append(i.text)

finalprice =[]

for i in price:
    finalprice.append(i.text)


finalratings =[]

for i in ratings:
    finalratings.append(i.text)

finalproductspec =[]

for i in productspec:
    finalproductspec.append(i.text)

# Using Pandas

Data = {'Product Name':finalproductname,'Price': finalprice,
        'Rating':finalratings}

range1 = range(1,25)
index =[]
for i in range1:
    index.append(i)

df = pd.DataFrame(Data,index)

print(df.to_string())

# df.to_csv(r'E:\Python\Python Project Files\SamsungPhones.csv')







