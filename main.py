from model.AirplaneM import Airplane
from model.VoyageM import Voyage
from model.employeeM import Employee

from logic.Airplane_LL import AirplaneLL
from logic.Voyage_LL import VoyageLL
from logic.Employee_LL import EmployeeLL

alpha = AirplaneLL("TF-CAR")
alpha.validate_plane_insignia()

test = EmployeeLL("HRABBA")
test.validate_name()