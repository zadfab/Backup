from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request

hdrs = {
    'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'} 
google_url = "https://www.ndtv.com/"
print("connecting...")
try:
    uclient = Request(google_url, headers=hdrs)
    html_page = uReq(uclient).read()

    print("NDTV news\n\n")

    page_soup = soup(html_page, "html.parser")

    # india all case
    # print(page_soup.h1)
    live_news = page_soup.find("div",{"class":"thumbnail"})
    print("Live Updates")
    print("\t\t\t", live_news.a.img["alt"])


    feature_news = page_soup.find("div", {"class": "featured_story"})

    print("Big story")
    print("\t\t\t", feature_news.div.a.img["title"])

    print("Top Stories")

    containers = page_soup.findAll("div", {"class": "thumbnail"})
    count = 1
    try:
        for container in containers:
            print("\t\t\t", count, ".", container.a.img["title"], "\n")
            print("")
            count += 1
    except TypeError:
        print("\t\t\tsubscribe for more ")



except :
    print("no internet")