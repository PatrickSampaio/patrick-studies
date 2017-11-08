class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True	

class Developer(Employee):
    raise_amt= 1.10  

    def __init__(self, first, last, pay, prog_lang):
        self.prog_lang = prog_lang
        Employee.__init__(self, first, last, pay) 

class Manager(Employee):
    
    #You should never pass an mutable argument as default, employees=[] XXXXX
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
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
            print(emp.fullname)

dev_1 = Developer('Corey', 'Schaffer', 50000, 'Python')
Developer_2 = Employee('Test', 'Fernandez', 60000)

print(dev_1.raise_amt)
print(Developer_2.raise_amt)

#print(help(Developer))
print(dev_1.prog_lang)

manager = Manager('Sue', 'Asgard', 90000, [dev_1, Developer_2])
print(manager.print_emps())

