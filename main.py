from model.AirplaneM import Airplane
from model.VoyageM import Voyage
from model.employeeM import Employee

from logic.Airplane_LL import AirplaneLL
from logic.Voyage_LL import VoyageLL
from logic.Employee_LL import EmployeeLL

alpha = AirplaneLL("F28")
alpha.validate_model()

test = EmployeeLL("HRABBA")
test.validate_name()