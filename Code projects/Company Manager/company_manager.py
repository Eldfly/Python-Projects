# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:17:38 2020

@author: Sofia


Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. 
Every one's pay is calculated differently, research a bit about it. 

After you've established an employee hierarchy, create a Company class that allows you to manage the employees. 
You should be able to hire, fire and raise employees.

"""
#
class Employee():
    
    employee_id = 100
    position = 'None'
    
    def __init__ (self, firstName, lastName):
        
        Employee.employee_id += 1   #for every new instance to the Emploýee class the id ins increased by one
        self.id = self.employee_id
        self.firstName = firstName
        self.lastName = lastName
       

class HourlyEmployee(Employee):
    
    total_hours_week = 0 
    rate_per_hour = 0
    salary_per_week = 0
    position = 'HourlyEmployee'
    
    def __init__ (self, firstName, lastName,total_hours_week=40,rate_per_hour=0):
        super().__init__(firstName, lastName)
        
        self.total_hours_week = total_hours_week
        self.rate_per_hour = rate_per_hour
    
    #calculate the salary earned every week
    @property
    def salary(self):
        
        self.salary_per_week = self.total_hours_week * self.rate_per_hour
        
        return self.salary_per_week

class SalariedEmployee(Employee):
      
    salary = 0
    position = 'SalariedEmployee'
    
    def __init__ (self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        
        self.salary = salary

class Manager(Employee):
    
    salary = 0
    bonus = 1.05
    total_salary = 0
    position = 'Manager'
    
    def __init__ (self, firstName, lastName, salary,bonus=0):
        super().__init__(firstName, lastName)
        
        self.salary = salary
        self.bonus = bonus
        self.total_salary = round(salary * bonus)
        
    def add_bonus(self, bonus):
        
        self.bonus = bonus
        self.total_salary = round(self.salary * bonus)
        

class Executive(Employee):
    
    salary = 0
    bonus = 1.10
    total_salary = 0
    position = 'CEO'
    
    def __init__ (self, firstName, lastName, salary,bonus=0):
        super().__init__(firstName, lastName)
        
        self.salary = salary
        self.bonus = bonus
        self.total_salary = round(salary * bonus)
    
    def add_bonus(self, bonus):
        
        self.bonus = bonus
        self.total_salary = round(self.salary * bonus)

class Company():
    
    company_id = 0
    employees = []
    
    def __init__ (self,name, orgNr, employees=None):
        
        self.company_id += 1
        self.id = self.company_id
        self.name = name
        self.orgNr = orgNr
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def view_employees(self):
        
        for emp in self.employees:
            print(str(emp.id) + ' ' + emp.firstName + ' ' + emp.lastName + ' ' + emp.position)
    
    def hire(self, employee):
        
        if employee not in self.employees:
            self.employees.append(employee)
    
    def fire(self, employee):
    
        if employee in self.employees:
            self.employees.remove(employee)
            return f'{employee.firstName} is fired from the company '
        else:
            return 'Employee does not exist in the company'
            
            
    def raise_position(self, employee, salary, bonus, typeofposition):
               
        self.typeofposition = typeofposition
        
        if employee in self.employees:
            
            if employee.position == 'CEO':
                print('Not possible to have a higher position')
                
            elif self.typeofposition == HourlyEmployee or self.typeofposition == SalariedEmployee:
                print('Not possible to raise the position to the lowest position in the company')
            else:
                employee.__class__ = typeofposition
                employee.salary = salary
                employee.bonus = bonus
                employee.total_salary = round(salary * bonus)
        else:
         print("can't find the employee in this company")

      
        
    