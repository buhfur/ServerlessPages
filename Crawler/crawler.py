import scrapy
import requests
import webbrowser
from bs4 import BeautifulSoup
#placeholder crawler


#try scraping a web page and writing it to a file


LINK = "https://en.wikipedia.org/wiki/Main_Page"



class GetPage:

    def __init__(self):


        self.SITE_URLS = {

        "wikipedia" : ["https://en.wikipedia.org/wiki/Main_Page"]
        }

    def scrape_page(self,url):

        #find the url in the dicionary
        _sitefile = ""
        
        for new in self.SITE_URLS.keys():
            if url in self.SITE_URLS[new]:
                _sitefile = new



        request = requests.get(url)
        with open(_sitefile, "w+") as site_file:
            try:
                site_file.write(request)
                print("file write successful")

            except Exception as e:
                print("couldent write to the file")


    def open_site(self,file_name):
        try:
            webbrowser.open(file_name)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    page = GetPage()
    page.scrape_page(LINK)
    page.open_site(LINK)
