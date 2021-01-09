
from bs4 import BeautifulSoup

from urllib.request import Request,urlopen


htmlParser = "lxml"
url='https://www.youtube.com/playlist?list=PL3D7BFF1DDBDAAFE5'
html=urlopen(url)
response=html.read()
soup=BeautifulSoup(response, htmlParser)
links = soup.find_all('a', attrs={'class':'pl-video-title-link'})
for a in links:
    print(a.get("href"))