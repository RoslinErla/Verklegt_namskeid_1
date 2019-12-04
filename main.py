from model.AirplaneM import Airplane
from logic.Airplane_LL import AirplaneLL


from model.VoyageM import Voyage
from logic.Voyage_LL import VoyageLL

from model.employeeM import Employee
from logic.Employee_LL import EmployeeLL

alpha = AirplaneLL("TF-CAR")
alpha.validate_plane_insignia()

test = EmployeeLL("HRABBA")
test.validate_name()