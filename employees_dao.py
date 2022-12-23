import settings
import psycopg2 as pg
from domain import *


def get_all():
    data = []
    with pg.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.user,password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute('select * from employees ORDER BY EMPLOYEE_iD DESC')
        for w in cursor:
            data.append(Employee(*w))
    return data

def get_one(id):
    with pg.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.user,password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from employees where employee_id={id}')
        w=cursor.fetchone()
        return Employee(*w)

def save(e):
    sql=f"insert into employees(first_name,last_name,salary,description) values ('{e.first_name}','{e.last_name}', {e.salary},'{e.description}')"
    with pg.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.user,password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        # print(w)
        # e=Employee(*w)
        # print(e)
        # return e

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