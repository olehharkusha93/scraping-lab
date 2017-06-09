import bs4
import json
import requests
import pandas
import csv
import seaborn as sb

url = 'http://www.imdb.com/chart/toptv/'
hdr = {'user-agent': 'Mozilla/5.0'}
req = requests.get(url, hdr)
if req.status_code == 200:
    print(req.headers['content-type'])
else:
    print(req.status_code)

soup = bs4.BeautifulSoup(req.text, 'html.parser')
#print(soup)

result = soup.select('.titleColumn a')
r = soup.select('.secondaryInfo')
rating = soup.select('.imdbRating')

with open('top_rated_tv_shows.csv', 'w', newline='') as csv_file:
    csv_app = csv.writer(csv_file)
    csv_app.writerow(['Title', 'Year', 'Rating'])
    for i, (item, t, t2) in enumerate(zip(result, r, rating)):
        csv_app.writerow([item.get_text(), t.get_text().strip('()'), t2.get_text().strip()])


file = pandas.read_csv('top_rated_tv_shows.csv', encoding='latin-1')
df1 = file['Rating']

sb.distplot(df1)
sb.plt.xlabel('Rating')
sb.plt.title('Top Rated TV Shows')
sb.plt.show()

#4
req = requests.get('http://www.cheapshark.com/api/1.0/stores')

if req.status_code == 200:
    data = req.json()
    print('Stores')
    for s in data:
        print(s['storeName'])
else:
    print(req.status_code)
