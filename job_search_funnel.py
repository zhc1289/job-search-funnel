from bs4 import BeautifulSoup
from urllib.request import urlopen
from webbrowser import open_new_tab
from shutil import copyfileobj

# to activate environment
# python -m venv env
# source ./env/bin/activate

url = "https://www.indeed.com/jobs?q=blockchain+$140,000&l=New+York+State&explvl=entry_level"

indeedFile = urlopen(url)
indeedHtml = indeedFile.read()
indeedFile.close()

# added parameter html parser to get rid of a parsing warning
soup = BeautifulSoup(indeedHtml, "html.parser")

count = 0
while count < 30:
    for item in soup.find_all('div', attrs={'class':'title'}):
        domain = 'https://www.indeed.com'
        link = item.find("a").get("href")
        page = "&start="+ str(count)
        link = domain + link + page
        with urlopen(link) as response, open('/home/zhi/Desktop/job_search_funnel/tester.txt', 'wb') as out_file:
            copyfileobj(response, out_file)
            open_new_tab(link)
        
        print(item.text)
    count += 10