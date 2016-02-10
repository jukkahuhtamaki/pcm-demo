# crawl_courses.py

from bs4 import BeautifulSoup

import requests 

response = requests.get('http://www.tut.fi/wwwoppaat/opas2015-2016/perus/laitokset/index.html')

print dir(response)
print response.content


soup = BeautifulSoup(response.content)
departments = soup.select('ul li ul li')

print departments
for department in departments:
  print department.text.strip()
  print department.select('a')