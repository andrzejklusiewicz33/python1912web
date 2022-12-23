import settings
import psycopg2 as pg
from domain import *


def get_all():
    data = [ ]
    with pg.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.user,
                    password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute('select * from products')
        for w in cursor:
            data.append(Product(*w))
    return data

# def get_all():
#     data = [
#         Product(1, "Bazuka", 1000, "Komenda leci w pył"),
#         Product(2, "Bulbulator", 200, "Urządzenie do bulgotania"),
#         Product(3, "Przyczłap do bulbulatora", 50, "Taki teges z takim tym że ten, z tym że nie do końca.")
#     ]
#     return data