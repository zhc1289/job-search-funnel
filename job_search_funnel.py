from bs4 import BeautifulSoup
from urllib.request import urlopen
from webbrowser import open_new_tab
from shutil import copyfileobj
import csv

# to activate environment
# python -m venv env
# source ./env/bin/activate

url = "https://www.indeed.com/jobs?q=blockchain%2B&l=New%2BYork%2BState&explvl=entry_level"

indeedFile = urlopen(url)
indeedHtml = indeedFile.read()
indeedFile.close()

# creates csv file to store jobs with links
f = csv.writer(open('results.csv', 'w'))
f.writerow(['Job titles and links to apply'])

# added parameter html parser to get rid of a parsing warning
soup = BeautifulSoup(indeedHtml, "html.parser")

count = 0
jobNumber = 0
while count < 70:

    for item in soup.find_all('div', attrs={'class':'title'}):
        
        # removes all sponsored jobs
        if item.parent.find('span', attrs={'class':'sponsoredGray'}):
            print(item)
            item.decompose()
        
        else:
            domain = 'https://www.indeed.com'
            link = item.find("a").get("href")
            page = "&start=" + str(count)
            link = domain + link + page

            
            # opens a new tab for each link
            # with urlopen(link) as response, open('/home/zhi/Desktop/job_search_funnel/tester.txt', 'wb') as out_file:
                #copyfileobj(response, out_file)
                #open_new_tab(link)

            # writes to csv file    
            f.writerow([item.text, link])
            jobNumber += 1       
 
    count += 10
f.writerow(["Number of Jobs:", jobNumber])