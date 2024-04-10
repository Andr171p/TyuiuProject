# html content parser:
from bs4 import BeautifulSoup
# fake web-driver:
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# fake User-agent:
from fake_useragent import UserAgent
# cian url:
from CIAN.CianParser.config import CIAN_URL
# time implicitly:
import time
# file work:
import os
# parse critical html:
from CIAN.CianParser.cian.critical import get_info, get_price, get_area, get_location, get_datetime, get_url
# ads dataframe:
import pandas as pd
import numpy as np


class PageScraper:
    def __init__(self, driver_version="122.0.6261.95"):
        # cian url:
        self.url = CIAN_URL
        # web-driver options:
        self.options = webdriver.ChromeOptions()
        # fake user-agent:
        self.user_agent = UserAgent().random
        # add options user-agent:
        self.options.add_argument(f"user-agent={self.user_agent}")
        # Chrome web-driver:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version=driver_version).install()),
                                       options=self.options)

    # this method get-requests on the url page:
    def get_requests(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    # this method parse links and return current links array:
    def parse_links(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        html_content = soup.find_all("a", attrs={"class": "_93444fe79c--link--VtWj6"})
        links = [link["href"] for link in html_content]

        return links

    # this method save html pages:
    def save_html_pages(self, links):
        try:
            for i in range(len(links)):
                self.driver.get(links[i])
                time.sleep(10)
                html_page = self.driver.page_source
                content = BeautifulSoup(html_page, "html.parser")
                with open(fr"C:\Users\andre\TyuiuProjectParser\TyuiuProjectParser\CIAN\CianParser\html_pages\html_page_{i + 1}.html",
                          "w", encoding="utf-8") as file:
                    file.write(str(content.prettify()))

        except Exception as _ex:
            print(f"[ERROR] : {_ex}")

    def save_url_pages(self, current_links):
        with open(r"C:\Users\andre\TyuiuProjectParser\TyuiuProjectParser\CIAN\CianParser\url_pages\links.txt",
                  "w", encoding="utf-8") as file:
            for link in current_links:
                file.write(link + "\n")

    # this method run parser:
    def run_parser(self):
        try:
            self.get_requests()
            links = self.parse_links()
            self.save_html_pages(links=links)
            self.save_url_pages(current_links=links)
        except Exception as _ex:
            print(f"[WARNING] : {_ex}")
        finally:
            self.driver.close()
            self.driver.quit()


class CianParser:
    def __init__(self):
        self.data = []

    def parse_html_file(self):
        directory = r"C:\Users\andre\TyuiuProjectParser\TyuiuProjectParser\CIAN\CianParser\html_pages"
        iterator = 0
        for filename in os.listdir(directory):
            elements = []
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                iterator += 1
                soup = BeautifulSoup(file, "html.parser")
                get_info(soup=soup, elements=elements)
                get_price(soup=soup, elements=elements)
                get_area(soup=soup, elements=elements)
                get_location(soup=soup, elements=elements)
                get_datetime(soup=soup, elements=elements)
                get_url(elements=elements, iterator=iterator)

            self.data.append(elements)

        ads = [row for row in self.data if None is not row]

        return ads


parser = CianParser()
data = parser.parse_html_file()
print(data)

