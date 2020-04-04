__author__ = "HAMIDULLAH Yasser"
__copyright__ = "Copyright 2020, MadaGeeksCar"
__credits__ = ["HAMIDULLAH Yasser"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "HAMIDULLAH Yasser"
__email__ = "yasserhamidullah@gmail.com"
__status__ = "Debug" 


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import urllib.request,re,os,sys
from driver_support import *
from config import *

#get the available driver
driver = get_available_driver()
if driver == "":
    print("can't find any available driver")
    sys.exit()

LOGIN_URL = "https://www.alphorm.com/account/login"
def login(username,password):
    #load the login page
    driver.get (LOGIN_URL)

    #fill username and password field
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id ("inputPassword1").send_keys(password)

    #find and click the login button
    driver.find_element_by_class_name("btn-connect").click()


def get_course(url):
    #load the course page
    driver.get (url)
    
    #get the course name
    course_name = url.split("/")[4][19:]
    print("Course : ",course_name)

    #create the course folder if not exists
    if not os.path.isdir(course_name):
        os.mkdir(course_name)
    
    #go to the pladetaillé tab
    driver.find_elements_by_class_name("title-tab-tuto")[1]

    #get the lesson list and count for the loop range
    lessons = driver.find_elements_by_class_name("video_plan")
    num_links = len(lessons)
    vid_number = 1
    #loop over the lessons
    for i in range(num_links):
        #click on a lesson
        lessons[i].click()

        #waiting util we can find the play button
        #element = WebDriverWait(driver, 10).until(lambda x:    x.find_element_by_class_name('jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback'))
        
        #play the selected lesson
        #driver.find_element_by_class_name("jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback").click()
        
        #get the page source for inspection
        page_soup = BeautifulSoup(driver.page_source, 'html.parser')

        #find the active lesson
        lesson = page_soup.find_all('div',class_="menu_point active")[0].div.div.a.text

        #find the active chapter
        chapter = page_soup.find_all('div',class_="menu_point active")[0].parent.p.text

        #get the video link for download
        video_link = page_soup.find_all('video',class_="jw-video jw-reset")[0]['src']
        
        #cleaning special chars
        chapter = re.sub("[!@#$%^&*()[]{};:,./<>?\|`~-=_+]", " ", chapter)
        chapter = chapter.replace("/","_")
        lesson = re.sub("[!@#$%^&*()[]{};:,./<>?\|`~-=_+]", " ", lesson)
        lesson = lesson.replace("/","_")

        #create chapter's folder if not exists
        if not os.path.isdir(course_name + "/" +chapter):
            os.mkdir(course_name + "/" +chapter)
            vid_number = 1
        
        #download and save to folder
        print("Downloading : ",chapter,"/",lesson,".mp4")
        urllib.request.urlretrieve(video_link, course_name+"/"+chapter+"/"+str(vid_number)+"-"+lesson+".mp4")
        vid_number += 1

    print("Finished")
login(email,password)

for url in courses:
    get_course(url)