# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:18:21 2020

@author: Sofia

Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. 
Every one's pay is calculated differently, research a bit about it. 

After you've established an employee hierarchy, create a Company class that allows you to manage the employees. 
You should be able to hire, fire and raise employees.

"""

from company_manager import Employee, Company, SalariedEmployee, HourlyEmployee, Manager, Executive


#create some employees
standard_emp = Employee('Sofia', 'Martinsson')
salary_emp = SalariedEmployee('Elsa', 'Persson', 50000)
hourly_emp = HourlyEmployee('Therese', 'Nilsson', 60, 190)
manager = Manager('Lisa', 'Carlsson', 60000, 1.06)
executive = Executive('Maja', 'Andersson', 80000, 1.12)


#check position for all the employees
print(executive.position)
print(manager.position)
print(salary_emp.position)
print(hourly_emp.position)

#create company
company = Company('IT Company', 'ABC-1234')


#hire employee
company.hire(salary_emp)
company.hire(executive)
company.hire(manager)
company.hire(hourly_emp)

#view all employees in company
company.view_employees()

#Fire Therese
company.fire(hourly_emp)

#view all employees in company
company.view_employees()

#raise the position for Elsa
print(salary_emp.salary)
print(salary_emp.bonus)
print(salary_emp.position)

company.raise_position(salary_emp,51000,1.04,Manager)
print(salary_emp.position)
print(salary_emp.salary)
print(salary_emp.bonus)

#add new bonus for Lisa (manager)
print(manager.bonus)
print(manager.total_salary)

print(manager.add_bonus(1.20))
print(manager.bonus)
print(manager.total_salary)

