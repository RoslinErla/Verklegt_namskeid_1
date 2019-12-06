from model.employeeM import Employee
from IO.employeeIO import employeeIO


a = employeeIO()
a.load_employee_from_file("status")
print(a)

inp = input()