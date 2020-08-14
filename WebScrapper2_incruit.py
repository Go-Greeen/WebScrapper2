import requests
from bs4 import BeautifulSoup
LIMIT = 20
URL = f"http://search.incruit.com/list/search.asp?col=job&il=y&kw=python"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("p", {"class": "sqr_paging sqr_pg_mid"}).find_all("a")
  last_page = pages[-3].get_text(strip=True)
  return int(last_page)


def extract_job(html):
  title = html.find("span", {"class":"rcrtTitle"})
  if title is not None:
    title = str(title.find("a").string)
  else:
    None
  print(title)



def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&startno={20*page}")
    soup = BeautifulSoup(result.text, "html.parser" )
    results = soup.find_all("li")
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs




def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs


