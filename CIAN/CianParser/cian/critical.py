from CIAN.Cian_Library.preproccesing_data import info_filter, string_to_sentence
from CIAN.Cian_Library.datetime_converter import current_date


# this function push info of ads in array:
def get_info(soup, elements):
    content = soup.find("div", attrs={"data-name": "ObjectFactoids"})
    info = string_to_sentence(content.text, mod="info")
    if info_filter(info):
        elements.append(info)
    else:
        elements.append(None)


# this function push price of ads in array:
def get_price(soup, elements):
    content = soup.find("div", attrs={"data-name": "OfferFactItem"})
    price = ''.join([i for i in content.text if i.isdigit()])
    elements.append(int(price))


# this function push area of ads in array:
def get_area(soup, elements):
    content = soup.find("div", attrs={"data-name": "OfferSummaryInfoLayout"})
    area = string_to_sentence(content.text, mod="area")
    elements.append(area)


# this function parse address of ads:
def get_location(soup, elements):
    content = soup.find("div", attrs={"data-name": "AddressContainer"})
    location = string_to_sentence(content.text, mod="location")
    elements.append(location)


# this function push datetime object in ads table:
def get_datetime(soup, elements):
    content = soup.find("span", attrs={"class": "a10a3f92e9--color_gray40_100--qPi9J a10a3f92e9--lineHeight_5u--e6Sug a10a3f92e9--fontWeight_normal--JEG_c a10a3f92e9--fontSize_14px--reQMB a10a3f92e9--display_block--KYb25 a10a3f92e9--text--e4SBY a10a3f92e9--text_letterSpacing__0--cQxU5"})
    date_time = string_to_sentence(content.text, mod="datetime")
    elements.append(current_date(date_time))


# this function push current url of ads page:
def get_url(elements, iterator):
    with open(r"C:\Users\andre\TyuiuProjectParser\TyuiuProjectParser\CIAN\CianParser\url_pages\links.txt",
              encoding="utf-8") as file:
        urls = file.read()
    array = [url for url in urls.split("\n")]

    elements.append(array[iterator - 1])

