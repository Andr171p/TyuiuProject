# web parsing/scrapping of page:
from bs4 import BeautifulSoup
# fake driver:
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# fake User-agent:
from fake_useragent import UserAgent
# fake proxies:
from Proxies.proxy import get_proxy
# links filter / replace token symbols:
from Project_Library.preprocessing_data import links_filter
# avito.ru url:
from AvitoParser.config import AVITO_URL
# driver time loop:
import time
# work with files directory:
import os
# avito parsing / scrapping:
from AvitoParser.avito.critical import get_info, get_price, get_area, get_location, get_datetime, get_url


class PagesLoader:
    def __init__(self, driver_version="122.0.6261.95"):
        # avito.ru page:
        self.url = AVITO_URL
        # web-driver options:
        self.options = webdriver.ChromeOptions()
        # fake User-agent:
        self.user_agent = UserAgent().random
        # add options user-agent:
        self.options.add_argument(f"user-agent={self.user_agent}")
        # Chrome web-driver:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version=driver_version).install()),
                                       options=self.options, seleniumwire_options=get_proxy())
        # init current links array:
        self.current_links = []
        # pages number:
        self.pages_number = 10

    # this method push get-request on the url page:
    def get_requests(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # this method return links of ads array:
    def parse_links(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        html_content = soup.find_all("a", attrs={"data-marker": "item-title"})
        links = [f"https://www.avito.ru{link["href"]}" for link in html_content]

        return links

    # this method write in file html code of current ads pages:
    def save_html_pages(self, links, count_current_page):
        try:
            for i in range(len(links)):
                if links_filter(links[i]):
                    self.current_links.append(links[i])
                    self.driver.get(links[i])
                    time.sleep(10)
                    html_page = self.driver.page_source
                    content = BeautifulSoup(html_page, "html.parser")
                    with open(fr"C:\Users\andre\PycharmProjects\Project.Avito.Parser\AvitoParser\html_pages\html_page_{count_current_page}.html",
                              "w", encoding="utf-8") as file:
                        file.write(str(content.prettify()))

                    return self.current_links

                else:
                    print("[INFO] this link is not useful")
        except Exception as _ex:
            print(f"[ERROR] : {_ex}")

    # this method write current links in txt file:
    def save_url_pages(self, current_links):
        with open(r"C:\Users\andre\PycharmProjects\Project.Avito.Parser\AvitoParser\url_pages\URL.txt", "w",
                  encoding="utf-8") as file:
            for link in current_links:
                file.write(link + "\n")

    def run_parser(self):
        try:
            current_page_count = 1
            for page_num in range(1, self.pages_number):
                self.get_requests(url=self.url + str(page_num))
                links = self.parse_links()
                current_links = self.save_html_pages(links, current_page_count)
                current_page_count += 1
                self.save_url_pages(current_links)
        except Exception as _ex:
            print(f"[ERROR] : {_ex}")
        finally:
            self.driver.close()
            self.driver.quit()


class AvitoParser:
    def __init__(self):
        self.data = []

    # this method parse html files in current directory:
    def parse_html_file(self):
        directory = r"C:\Users\andre\PycharmProjects\Project.Avito.Parser\AvitoParser\html_pages"
        iterator = 0
        for filename in os.listdir(directory):
            elements = []
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                iterator += 1
                soup = BeautifulSoup(file, "html.parser")
                get_info(soup, elements)
                get_price(soup, elements)
                get_area(soup, elements)
                get_location(soup, elements)
                get_datetime(soup, elements)
                get_url(elements, iterator)

            self.data.append(elements)

        return self.data

