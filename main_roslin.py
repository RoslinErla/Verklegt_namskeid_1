from model.employeeM import Employee
from IO.employeeIO import EmployeeIO


a = EmployeeIO()
a.load_employee_from_file("status")
print(a)

inp = input()