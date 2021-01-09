from bs4 import BeautifulSoup as soup
from urllib.request import Request,urlopen

hdrs = {
    'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

google_url  = "https://www.mygov.in/covid-19/"

uclient = Request(google_url,headers=hdrs)
html_page = urlopen(uclient).read()

page_soup = soup(html_page,"html.parser")
containers = page_soup.findAll("div",{"class":"iblock_text"})

case_name = ["Active Cases : \n\t\t\t\t","Recovered Cases :\n\t\t\t\t","Total Deaths :\n\t\t\t\t","Total Migration :\n\t\t\t\t"]
count = 0
total_cases = 0
for container in containers:

    print("{0}{1}".format(case_name[count],container.span.text))
    while count <2:
        total_cases = total_cases + int(container.span.text.replace(",",""))
        break
    count+=1
print("Total cases :\n\t\t\t\t",total_cases)

print("All cases by states : ")
containers = page_soup.findAll("div",{"class":"views-row"})
st_number = page_soup.findAll("span",{"class":"st_number"})
count = 1
cases = []
states = []
for i in  containers:
    states.append(i.span.text)
for i in st_number:
    cases.append(i.text)

for i in range(len(states)):
    print("\n\t\t\t\t",count,states[i],":",cases[i])
    count += 1