import settings
import psycopg2 as pg
from domain import *


def get_all():
    data = []
    with pg.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.user,password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute('select * from employees')
        for w in cursor:
            data.append(Employee(*w))
    return data

#PGBENCH + PGBENCH TOOLS
#return Employee.query.filter(salary>1000).all()

# public List<Employee> get_all(): #java

# def get_all():
#     data = [
#         Employee(1, "Tomasz", "Mrzygłód", 10000, "Fajny kolega  z zespołu, szkoda że weganin"),
#         Employee(2, "Janusz", "Polak", 2000, "Typowy Janusz (wiadomo, brzuch i wąsy ;) )"),
#         Employee(3, "Nosacz", "Socjalny", 5000, "Siedzi na socjalu i jeszcze narzeka")
#     ]
#     return data

# def funkcja(x:int):
#     print(x)
#
# funkcja('dupa')