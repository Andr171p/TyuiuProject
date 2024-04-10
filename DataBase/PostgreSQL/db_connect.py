import psycopg2
from DataBase.PostgreSQL.db_auth_data import host, user, password, db_name, port
from AVITO.AvitoParser.parser import AvitoParser
from CIAN.CianParser.parser import CianParser


parser = CianParser()
data_parser = parser.parse_html_file()

connection = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port
)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO komerc (information, price, area, address, datas, url) VALUES (%s, %s, %s, %s, %s, %s)"
        for row in data_parser:
            cursor.execute(sql, row)

        connection.commit()
except Exception as _ex:
    print("[INFO] Error while working with PostgresSQL", _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("[INFO] PostgresSQL connection closed")

