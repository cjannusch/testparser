import requests
from Bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=dow+jones&rlz=1C1GCEA_enUS778US778&oq=dow+jones&aqs=chrome..69i57.3565j0j7&sourceid=chrome&ie=UTF-8'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

job_elems = results.find_all('section', class_='IsqQVc NprOob XcVN5d')

for job_elem in job_elems:
    print(job_elem)

print('test1234')
