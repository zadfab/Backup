from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card"
print("Downloading page...")
uclient = ureq(my_url)

page_html = uclient.read()

with open('newegg.html', 'w') as fp:
    fp.write(str(page_html))

uclient.close()
# html_parser
page_soup = soup(page_html, "html.parser")
print(page_soup.h1.text, "\n")
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "Graphic_card.csv"
try:
    with open(filename, "w") as f:
        header = "Brand, Product_name, Shipping, Indian_shipping\n"
        f.write(header)

        for container in containers:
            brand = container.div.div.a.img["title"]
            product_name = container.a.img["title"]
            price = container.find("li", {"class": "price-current"})
            price = price.strong.text
            ind_price = (73 * (int(price)))
            print("Brand : ", brand)
            print("product : ", product_name)
            print("price of product : ", price + '$', "Indian price :", ind_price)
            print("------------------------------------------------------------")

            f.write(
                brand + "," + product_name.replace(",", "|") + "," + price + "$" + "," + str(ind_price) + "rs" + "\n")
except PermissionError:
    print("close the file and try again!")
