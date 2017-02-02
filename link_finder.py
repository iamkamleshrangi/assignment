# coding=utf-8
from bs4 import BeautifulSoup
import requests
import re
class LinkFinder():

    #initializing of the function
    def __init__(self):
        self.naukri_url = 'https://www.naukri.com'
        self.linkedin_url = 'https://www.linkedin.com'
        self.links = set()
    #Error message function
    def error(self,message):
        pass

    #Search for tag into HTML
    def handle_starting(self,tag,attrs):
        print tag

    #customize for website to website
    def handle_naukri_starting(self,soup):
        data_set = set()
        for listAll in soup.find_all(attrs={"class": "browseIndustry section_white_title"}):
            for data in listAll.find_all(attrs={"class": "multiColumn colCount_four"}):
                for link in data.find_all("a"):
                    url = link.get("href").split("?")[0]
                    self.links.add(url)
        print self.links

    #For the cleaning of the data
    def cleaner(self, str):
        strng = ''
        if type(str) != type(""):
            str = str.encode(encoding='UTF-8', errors='strict')
        str = re.sub('[^a-zA-Z0-9-_*.]', ' ', str)
        str = re.sub('[ áá âââââââââââââ¯âãï»¿]+', ' ', str)
        for word in str.split(" "):
            strng += "%s " % (word.strip())
        return strng.strip().lower()

obj = LinkFinder()
