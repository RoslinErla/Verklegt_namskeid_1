from model.AirplaneM import Airplane
from IO.airplaneIO import AirplaneIO

from model.employeeM import Employee
from IO.employeeIO import EmployeeIO


a = AirplaneIO()
a.load_airplane_from_file()
print(a)



def print_employee():
    a = EmployeeIO()
    a.load_employee_from_file("status")
    print(a)

inp = input()