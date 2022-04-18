from bs4 import BeautifulSoup
import pandas as pd 
import requests
from datetime import datetime


def extract(page):
     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
     url = f'https://ph.indeed.com/jobs?q=Python&start={page}&vjk=067f5ef9079fba15'
      
     r = requests.get(url, headers)
     soup = BeautifulSoup(r.content, 'html.parser')
     return soup
     


def transform(soup):

     divs = soup.find_all('div', class_ = 'slider_container css-11g4k3a eu4oa1w0')
     for item in divs:
          title = item.find('h2', class_ = 'jobTitle').text.strip()
          company = item.find('span', class_ = 'companyName').text.strip()

          try:
               salary = item.find('div', class_="metadata salary-snippet-container").text.strip()
          except:
               salary = ''

          try:
               location = item.find('div', class_ = 'companyLocation').text.strip()
          except:
               location = '' 


          try:
               status = item.find('tr', class_ = 'jobCardShelf').text
          except:
               status = 'Not specified'
          
          date = item.find('span', class_ = 'date').text

          summary = item.find('div', class_ = 'job-snippet').text.strip().replace('\n', "")
          
          dateRetrive = datetime.now()
          job = {
               'title': title,
               'company': company,
               'location': location,
               'salary': salary,
               'Date Retrive': dateRetrive,
               'Job Date': date,
               'Status': status,
               'summary': summary
          }

          joblist.append(job)

     return

joblist = []

try: 
     for i in range(0,2000 ):

          print(f'getting page {i}')
          c = extract(i)
          transform(c)
except:
     print(f"{'>' * 20 }No more Data {'<' * 20 }")

df = pd.DataFrame(joblist)
print(df)

df.to_csv("new.csv")