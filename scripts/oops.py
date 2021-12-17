#
#
# class Employee:
#     num_of_employees = 0
#     raise_amount = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + '@company.com'
#         Employee.num_of_employees += 1
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     ## Class method
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first,last,pay)
#         self.prog_lang = prog_lang
#
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         if employees is None:
#             self.emplyees = []
#         else:
#             self.emplyees = employees
#         def add_emp(self, emp):
#             if emp not in self.emplyees:
#                 self.emplyees.append(emp)
#
#
# emp_1 = Employee('fayaz', 'sayyed', 5000)
# #emp_2 = Employee()
#
# #
# # print(emp_1)
# # print(emp_2)
#
# # print(emp_1.email)
# # print('{} {}'.format(emp_1.first,emp_1.last))
# # print(emp_1.pay)
# # emp_1.apply_raise()
# # #Employee.set_raise_amt(1.5)
# # emp_str_1 = 'John-Doe-7000'
# # emp_str_2 = 'Steve-Smith-6000'
# # #first, last, pay = emp_str_1.split('-')
# # new_emp_1 = Employee.from_string(emp_str_1)
# # new_emp_2 = Employee.from_string(emp_str_2)
# # Employee.raise_amount = 1
# # emp_1.set_raise_amt(1.07)
# # print(emp_1.raise_amount)
# # print(Employee.raise_amount)
# # print(new_emp_2.email)
# dev_emp_1 = Developer('Corey', 'Schafer', 500000, 'python')
# #dev_emp_2 = Developer(emp_str_2)
# # print(dev_emp_1.email)
# # #
# # import datetime
# # mydate = datetime.date(2016, 7, 11)
# # print(Employee.is_workday(mydate))
# print(dev_emp_1.pay)
# dev_emp_1.apply_raise()
# print(dev_emp_1.email)
# print(dev_emp_1.prog_lang)




'''My first class'''
class Employee():
    raise_amount = 1.04
    employee_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + '.' + last + '@company.com'
        Employee.employee_count += 1
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    def __repr__(self):
        return "{}, {}, {}".format(self.first,self.last,self.pay)
    def __str__(self):
        return "{} - {}".format(self.first,self.last)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay, prog_lang):
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

#emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1 = Employee.from_string('corey-schafer-50000')
dev_1 = Developer('Test', 'User', 60000, 'python')

# print(dev_1.prog_lang)
# print(dev_1.fullname())
# print(dev_1.employee_count)

mgr_1 = Manager('Sue', 'Smith', 10000, [dev_1])
#emp_1.first = 'Jim'
# print(emp_1.email)
emp_1.fullname = 'Fayaz Hussain'
print(emp_1.email)

del emp_1.fullname
























