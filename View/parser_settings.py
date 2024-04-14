from AVITO.AvitoParser.parser import PagesLoader, AvitoParser
from CIAN.CianParser.parser import PageScraper, CianParser
from DataBase.PostgreSQL.db_connect import db_connect
from View.filter import check_doubles


def start_pages_load():
    avito = PagesLoader()
    # cian = PageScraper()

    avito.run_parser()
    # cian.run_parser()


def start_parser():
    avito_parser = AvitoParser()
    cian_parser = CianParser()

    avito_data = avito_parser.parse_html_file()
    cian_data = cian_parser.parse_html_file()
    for items in cian_data:
        avito_data.append(items)

    data = check_doubles(avito_data)

    return data


def save_in_database(data):
    db_connect(data)


start_pages_load()

