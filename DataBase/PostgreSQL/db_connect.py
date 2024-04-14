import psycopg2
from DataBase.PostgreSQL.db_auth_data import host, user, password, db_name, port


def db_connect(data_parser):
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

