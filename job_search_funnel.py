from bs4 import BeautifulSoup
from urllib.request import urlopen

# to activate environment
# python -m venv env
# source ./env/bin/activate

url = "https://www.indeed.com/jobs?q=blockchain+$140,000&l=New+York+State&explvl=entry_level"

indeedFile = urlopen(url)
indeedHtml = indeedFile.read()
indeedFile.close()

# added parameter html parser to get rid of a parsing warning
soup = BeautifulSoup(indeedHtml, "html.parser")

for item in soup.find_all('div', attrs={'class':'title'}):
    domain = 'https://www.indeed.com'
    link = item.find("a").get("href")
    link = domain + link
    print(item.text)
    print(link)