'''Method == Function'''
'''Attribute == class'''

class Employee:
    #pass
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
       # Employee.__init__(self, first, last, pay)
        self.prog_lang  = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
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
        for emp in self.employees:
            print('-->', emp.fullname())






# emp_1 = Employee('Fayaz', 'sayyed', 6000)
# emp_2 = Employee('fayaz', 'syed', 5000)



# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)

# import datetime
# my_date = datetime.date(2016, 6, 10)
# print(Employee.is_workday(my_date))
# print(new_emp_1.email)
# print(new_emp_1.pay)
emp_2 = Developer('fayaz', 'syed', 5000, 'python')
#dev_1 = Developer.from_string(emp_2)
# print(emp_2.prog_lang)
# # emp_2.apply_raise()
# print(emp_2.email)

mgr_1 = Manager('sue', 'Smith', 9000, [emp_2])
mgr_1.add_emp(emp_2)
print(mgr_1.email)







