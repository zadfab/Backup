from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
hdrs = {
    'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

my_url = "https://www.bbc.com/"

uclient = Request(my_url,headers=hdrs)
html_page = urlopen(uclient).read()

page_soup = soup(html_page,"html.parser")
for i in range(1,6):
    container = page_soup.find("li",{"class":"media-list__item media-list__item--{0}".format(i)})
    print(container.div.a.text)

