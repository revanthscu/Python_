import requests as req
import pandas as pd
from bs4 import BeautifulSoup


baseurl = 'https://www.fragrantica.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

df1 = pd.DataFrame()
r1 = req.get('https://www.fragrantica.com/search/', headers=headers)

'''lxml is a html parser'''
soup = BeautifulSoup(r1.content, 'lxml')

productlist = soup.find_all('div', class_="cell card fr-news-box")
productlinks = []
for item in productlist:
    for name in item.find_all('a', href = True):
        print(name.text.strip())
        productlinks.append(baseurl +name['href'])
        df = pd.DataFrame({'Perfume_Name':[name.text.strip()], 'Perfume_Links': [baseurl +name['href']]})
        df1 = df1.append(df, ignore_index=True)
print(productlinks)

print(df1)
df1.to_csv('Fragrantica_searchpage_info.csv')
'''r = req.get('https://www.fragrantica.com/perfume/Givenchy/Amarige-3.html', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


Finding perfume brand name
name = soup.find('h1', itemprop='name').text.strip()
Finding the ratings
rating = soup.find('span', itemprop="ratingValue").text.strip()
print(name,'--->',rating)'''

