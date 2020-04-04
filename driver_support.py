from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import urllib.request,re,os
import config
def get_available_driver():
    driver = ""
    if config.firefox_driver_path != "":
        try:
            driver = webdriver.Firefox(executable_path=config.firefox_driver_path)
        except:
            print("firefox driver path is not set correctly | the selected driver doesn't match your firefox installed browser")
    elif config.chrome_driver_path != "":
        try:
            driver = webdriver.Chrome(executable_path=config.chrome_driver_path)
        except:
            print("chrome driver path is not set correctly | the selected driver doesn't match your installed chrome browser")
    elif config.microsoft_edge_driver_path != "":
        try:
            driver = webdriver.Edge(executable_path=config.chrome_driver_path)
        except:
            print("microsoft edge driver path is not set correctly | the selected driver doesn't match your installed microsoft edge browser")
    elif config.safari_driver_path != "":
        try:
            driver = webdriver.Safari(executable_path=config.chrome_driver_path)
        except:
            print("safari driver path is not set correctly | the selected driver doesn't match your installed safari browser")
    else:
        return driver
    return driver