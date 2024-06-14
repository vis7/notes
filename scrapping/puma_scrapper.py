import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

# get element with id
results = soup.find(id="ResultsContainer")
# print(results.prettify())

# find element by class name
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title = job_element.find("h2", class_='title')
    company = job_element.find("h3", class_='company')
    location = job_element.find("p", class_='location')
    # print(title.text.strip())
    # print(company.text.strip())
    # print(location.text.strip())
    # print()

# find string name by class name and text content
python_jobs = results.find_all(
    "h2",
    string= lambda x: "python" in x.lower()
)

for python_job in python_jobs:
    title = python_job.find('h2', class_='title')
    company = python_job.find('h3', class_='company')
    location = python_job.find('p', class_='location')
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()

 # The .descendants attribute lets you iterate over all of a tag’s children, recursively: its direct children, the children of its direct children, and so on:

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# Puma Scrapper websmith task
domain = "https://in.puma.com"

# puma scrapper
name_elements = soup.find_all("h3", class_="w-full mobile:text-sm mobile:pr-0 font-bold text-base pr-5 line-clamp-2")
price_elements = soup.find_all("div", class_="flex flex-col flex-none mobile:items-start items-end text-sm md:text-base mobile:mt-2")
link_elements = soup.find_all("a", class_="tw-hqslau tw-xbcb1y")

name = name_elements[0].contents[0]
price = price_elements[0].span.string

# change link and continue untill it keeps going and find color from it and store it
link1 = domain + link_elements[1].get("href")
link2 = link1.replace('01','03')


response = requests.get(link1)

page2 = BeautifulSoup(response.content, 'html.parser')
color = page2.find('h4').contents[0]


