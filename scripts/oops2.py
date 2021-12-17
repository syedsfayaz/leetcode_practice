class Employee():
    num_of_emps = 0
    raise_amount = 5 #   '''Class variable'''

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.fullname = self.first + self.last

        Employee.num_of_emps += 1
    @property
    def email(self):
        #self.email = self.first + '.' + self.last + '@gmail.com'
        return self.first + '.' + self.last + '@gmail.com'
    @property
    def fullname(self):
        #self.fullname = self.first + self.last
        #return self.fullname
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Full Name')
        self.first = None
        self.last = None

    def __add__(self, other):
        return self.pay + other.pay


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 1:
            return False
        return True


### Subclasses
class Developer(Employee):
    raise_amount = 20
    def __init__(self, first, last, pay,  language):
        super().__init__(first, last, pay)
        self.language = language
    def __repr__(self):
        print('{} {} {}'.format(self.first, self.last, self.email))

class Manager(Employee):
    def __init__(self, first, last, pay,  employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        #if len(self.employees) != 0:
        #print(self.employees)
        for emp in self.employees:
            print(emp.fullname())
    # def __str__(self):
    #     print('{} {} {}'.format(self.first,self.last,self.email))

    def __repr__(self):
        return('{} {} {}'.format(self.first, self.last, self.email))




E1 = Developer('jay', 'veeru', 50000, 'python')
E2 = Developer('jaya', 'eru', 60000, 'Java')
#E1.first = 'aka'
# print(E1.first)
# print(E1.email)
# print(E1.fullname)
# E1.fullname = 'Fayaz Sayyed'
# print(E1.first)
# print(E1.email)
# del E1.fullname
# print(E1.first)


# mgr1 = Manager('sue', 'collins', 5000, [E1])
#
# #print(mgr1.email)
# #mgr1.print_emps()
# # mgr1.add_emp(E2)
# # mgr1.remove_emp(E1)
# # mgr1.__str__()
# #print(E1 + E2)
# print(float.__add__(10.5,5))
# print('lenth'.__len__())

''' Decorator function'''
from functools import wraps

def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

#### Logger function
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

@decorator_function
def display():
    print('display function ran')

# @decorator_function
#@my_logger
import  time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('Hunk',25)
# display()

#

# class decorator_class(object):
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#     def __call__(self, *args, **kwargs):
#         print('Call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
# @decorator_class
# def display():
#     print('display function ran')
#
# display()
#
# @decorator_class
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name,age))
#
# display_info('John', 25)










