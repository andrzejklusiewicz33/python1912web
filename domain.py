class Fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Author:
    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

class Employee:
    def __init__(self,employee_id,first_name,last_name,salary,description):
        self.employee_id=employee_id
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
        self.description=description
    def __str__(self):
        return str(self.__dict__)