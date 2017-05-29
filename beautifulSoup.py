import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# for url in soup.find_all('a'):
#     print(url.get('href'))

# Example for tag with class
# for div in soup.find_all('div', class_='body'):
#     print(div.text)

# Example for table scrape
# table = soup.table
# table_rows = table.find_all('tr')
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

# Pandas version for table scrape
# import pandas as pd
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
# for df in dfs:
#     print(df)

sitemap = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
smap = bs.BeautifulSoup(sitemap, 'xml')

for url in smap.find_all('loc'):
    print(url.text)
