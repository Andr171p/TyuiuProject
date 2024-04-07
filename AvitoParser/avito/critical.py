# html parsing / scrapping:
from bs4 import BeautifulSoup
# prepare data:
from Project_Library.preprocessing_data import replace_symbol
# convert to datetime:
from Project_Library.datetime_converter import current_date
from datetime import date


# this function return info of sector --> str:
def get_info(soup, elements):
    content = soup.find("h1", attrs={"data-marker": "item-view/title-info"})
    info = replace_symbol(content.text)[14:-13]
    elements.append(info)


# this function return price per m^2 of sector --> int:
def get_price(soup, elements):
    content = soup.find("div", attrs={"class": "style-item-price-sub-price-_5RUD"})
    price = content.text.replace("\n", "").replace("\xa0", " ").replace(" ", "")[:-8]
    elements.append(int(price))


# this function return area of sector --> float:
def get_area(soup, elements):
    content = soup.find("li", attrs={"class": "params-paramsList__item-_2Y2O"})
    area = replace_symbol(content.text).replace(" ", "")[8:-4]
    elements.append(float(area))


# this function return location of sector --> str:
def get_location(soup, elements):
    content = soup.find("span", attrs={"class": "style-item-address__string-wt61A"})
    location = replace_symbol(content.text)[17:-16]
    elements.append(location)


# this function return datetime of ads --> datetime object:
def get_datetime(soup, elements):
    try:
        content = soup.find("span", attrs={"data-marker": "item-view/item-date"})
        date_time = f"· {replace_symbol(content.text)[50:-15]}"
        elements.append(current_date(date_time))
    except Exception as _ex:
        print(f"[WARNING] : {_ex}")
        elements.append(date.today())


# this function return url of ads page:
def get_url(elements, iterator):
    with open(r"C:\Users\andre\PycharmProjects\Project.Avito.Parser\AvitoParser\url_pages\URL.txt",
              encoding="utf-8") as file:
        urls = file.read()
    array = [url for url in urls.split("\n")]

    elements.append(array[iterator - 1])

