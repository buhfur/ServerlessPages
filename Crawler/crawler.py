import Scrapy
import requests
import webbrowser
from bs4 import BeautifulSoup
#placeholder crawler


#try scraping a web page and writing it to a file


LINK =  "https://en.wikipedia.org/wiki/Main_Page"



class GetPage:
    def scrape_page(self, LINK):
        request = requests.get(LINK)
        with open("{}", "w+").format(LINK) as site_file:
            try:

                site_file.write(request)
            except Exception as e:
                print("couldent write to the file")


    def open_site(self, file_name):
        try:
            webbrowser.open(file_name)
        except Exception as e:
            print(e)
            
