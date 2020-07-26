import requests
from bs4 import BeautifulSoup
import re

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
cookies ='__mta=187036567.1595679127410.1595681896675.1595688480461.16; uuid_n_v=v1; uuid=0C6F2110CE7011EAB0594FFAA70EE9CE72BDC126374A4E99941F5D2FCC090317; _csrf=65edc23e9ad8e40b105668fc464ffbf956aeacfef30324fc556dd8475e717bbd; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=17385e32d3fc8-0952eeacfd5bac-31637404-fa000-17385e32d3fc8; _lxsdk=0C6F2110CE7011EAB0594FFAA70EE9CE72BDC126374A4E99941F5D2FCC090317; mojo-uuid=01314b3bc31c11a555085a9add2a79da; mojo-session-id={"id":"f69bd4894c58cb49492c973fbccf6310","time":1595687426801}; mojo-trace-id=6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595679125,1595679338,1595688548; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595688548; __mta=187036567.1595679127410.1595688480461.1595688547931.17; _lxsdk_s=1738661d211-437-5ad-650%7C%7C13'
headers = {'User-Agent':user_agent, 'Cookie':cookies}
url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
movie_list = soup.find('dl', attrs={'class': 'movie-list'})

content =[]
for movie in movie_list.find_all('dd',limit=10):
    title = movie.find('div', attrs={'class':'movie-hover-title'}).get('title')
    pattern = re.compile('.*类型.*?</span>(.*?)</div>.*上映时间.*?</span>(.*?)</div>',flags=re.S)
    result = re.search(pattern,str(movie))
    movie_type = result.group(1).strip()
    movie_date = result.group(2).strip()
    movie_item = title+','+movie_type+','+movie_date
    content.append(movie_item)

with open('maoyantest.csv','a+',encoding='utf-8') as article:
    for item in content:
        article.write(item)
        article.write('\n')
