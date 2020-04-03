from bs4 import BeautifulSoup
import urllib.request,os,re
import zipfile
import requests
from lxml import html


login_url = "https://www.alphorm.com/account/login"
"""result = session_requests.get(login_url)
payload = {
	"UserName": "barydadaboys@gmail.com", 
	"Password": "Yasserpc&", 
}
tree = html.fromstring(result.text)
result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

url = 'https://www.alphorm.com/profil/monprofil'
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)
"""
#get the the soup_scrape_parsed
def get_soup(url):
  response = requests.get(
	url, 
	headers = dict(referer = url)
)
  return BeautifulSoup(response.text, 'html.parser')

def get_vid_url(soup):
  div_pl1 = soup.find_all('script')
  idx = ""
  for idk,s in enumerate(div_pl1):
    if "idVideoInit" in s.text:
      idx=idk
      break
  if idx=="":
    return "not found"
  tag = div_pl1[idx]
  
  vr = str(tag).split("\n")[4]
  return vr.split(" ")[15][1:-3]

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

url = "https://www.alphorm.com/tutoriel/formation-en-ligne-excel-2016-niveau-expert-2-2"
course_name = url.split("/")[4][19:]
if not os.path.isdir(course_name):
  os.mkdir(course_name)
get_vid_url(get_soup(url))
html_soup = get_soup(url)
div_pl = html_soup.find_all('a',class_="cursor video_plan")
chapter = ""
video = "" 
#print(get_soup(url))
for a in div_pl:
  chapter = a.parent.parent.parent.parent.p.text
  chapter = re.sub("[!@#$%^&*()[]{};:,./<>?\|`~-=_+]", " ", chapter)
  chapter = chapter.replace("/","_")
  video = a.text
  video = re.sub("[!@#$%^&*()[]{};:,./<>?\|`~-=_+]", "_", video)
  video = video.replace("/","_")
  if not os.path.isdir(course_name + "/" +chapter):
    os.mkdir(course_name + "/" +chapter)
  print("===>",video)
  print("==>",get_vid_url(get_soup("https://www.alphorm.com"+a['href'])))
  print("ererer===>https://www.alphorm.com"+a['href'])
  #urllib.request.urlretrieve(get_vid_url(get_soup("https://www.alphorm.com"+a['href'])), course_name+"/"+chapter+"/"+video+".mp4")