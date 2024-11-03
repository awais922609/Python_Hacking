from bs4 import BeautifulSoup
import requests

url = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
).text

soup = BeautifulSoup(url, 'html.parser')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# print(jobs)

for job in jobs:
    published_date = job.find('span', class_="sim-posted").text.strip()
    if 'few' in published_date or 'a few' in published_date:
        more_info = job.header.h2.a['href']
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        job_desc = job.find('ul', class_="list-job-dtl clearfix").text.strip()
        skills = job.find('span', class_="srp-skills").text.strip()
        print(f"Compan Name: {company_name}")
        print(f"{job_desc}")
        print(f"more_info: {more_info}")
        print('\n\n')
