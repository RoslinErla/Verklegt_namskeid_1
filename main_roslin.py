from model.employeeM import Employee
from IO.employeeIO import employeeIO


a = employeeIO()

print(a.load_employee_from_file("alpha"))