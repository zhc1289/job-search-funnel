from bs4 import BeautifulSoup
from urllib.request import urlopen
from webbrowser import open_new_tab
from shutil import copyfileobj
from pyautogui import typewrite, time, hotkey, PAUSE, FAILSAFE
import csv, time

# to activate environment
# python -m venv env
# source ./env/bin/activate

# need to install bs4 and pyautogui
# pyautogui failsafe moving mouse to upperleft of screen will stop the program
FAILSAFE = True

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
while count < 19:

    for item in soup.find_all('div', attrs={'class':'title'}):
        
        # removes all sponsored jobs
        if item.parent.find('span', attrs={'class':'sponsoredGray'}):
            item.decompose()

        # removes all jobs that have me apply through company site instead of Indeed resume
        elif not item.parent.find('span', attrs={'class':'iaLabel'}):
            domain = 'https://www.indeed.com'
            link = item.find("a").get("href")
            page = "&start=" + str(count)
            link = domain + link + page

            # opens a new tab for each apply through company link
            with urlopen(link) as response, open('/home/zhi/Desktop/job_search_funnel/tester.txt', 'wb') as out_file:
                copyfileobj(response, out_file)
                open_new_tab(link)

            # writes to csv file
            f.writerow([item.text, link])
            jobNumber += 1   
            item.decompose()
        
        else:
            domain = 'https://www.indeed.com'
            link = item.find("a").get("href")
            page = "&start=" + str(count)
            link = domain + link + page

            with urlopen(link) as response, open('/home/zhi/Desktop/job_search_funnel/tester.txt', 'wb') as out_file:
                copyfileobj(response, out_file)
                open_new_tab(link)
                time.sleep(2)
                hotkey('ctrl', 'w')

            f.writerow([item.text, link])
            jobNumber += 1       
 
    count += 10
f.writerow(["Number of Jobs:", jobNumber])